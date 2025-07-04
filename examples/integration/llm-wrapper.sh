#!/bin/bash
# Wrapper script for LLM CLI tools that captures prompts before execution
# This can be used with tools like GitHub Copilot CLI, Claude CLI, etc.

# Configuration
PROMPT_CAPTURE_ENABLED=${PROMPT_CAPTURE_ENABLED:-true}
LLM_TOOL=${LLM_TOOL:-"claude"}  # Change this to your LLM tool
LLM_MODEL=${LLM_MODEL:-"claude-3-opus"}

# Function to capture prompt
capture_prompt() {
    local prompt="$*"
    
    if [ "$PROMPT_CAPTURE_ENABLED" != "true" ]; then
        return 0
    fi
    
    # Save prompt for next commit
    echo "$prompt" > .current-llm-prompt
    echo "$LLM_MODEL" > .current-llm-model
    
    # Also save to prompts directory with timestamp
    if [ -d ".prompts" ]; then
        local timestamp=$(date +%Y%m%d-%H%M%S)
        local prompt_file=".prompts/sessions/session-${timestamp}.json"
        
        mkdir -p ".prompts/sessions"
        
        cat > "$prompt_file" << EOF
{
    "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
    "prompt": "$prompt",
    "model": "$LLM_MODEL",
    "tool": "$LLM_TOOL",
    "cwd": "$(pwd)",
    "git_branch": "$(git branch --show-current 2>/dev/null || echo 'none')",
    "uncommitted_changes": $(git status --porcelain | wc -l)
}
EOF
    fi
}

# Function to execute LLM tool
execute_llm() {
    local prompt="$*"
    
    case "$LLM_TOOL" in
        claude)
            # Example for Claude CLI
            claude "$prompt"
            ;;
        copilot)
            # Example for GitHub Copilot CLI
            gh copilot suggest "$prompt"
            ;;
        openai)
            # Example for OpenAI CLI
            openai api completions.create -m "$LLM_MODEL" -p "$prompt"
            ;;
        *)
            echo "Unknown LLM tool: $LLM_TOOL" >&2
            exit 1
            ;;
    esac
}

# Main execution
if [ $# -eq 0 ]; then
    echo "Usage: $0 <prompt>"
    echo ""
    echo "Environment variables:"
    echo "  LLM_TOOL              - LLM tool to use (default: claude)"
    echo "  LLM_MODEL             - Model to use (default: claude-3-opus)"
    echo "  PROMPT_CAPTURE_ENABLED - Enable prompt capture (default: true)"
    exit 1
fi

# Capture the prompt
capture_prompt "$@"

# Execute the LLM tool
execute_llm "$@"

# Check if there were code changes and suggest commit
if [ "$PROMPT_CAPTURE_ENABLED" = "true" ] && [ -f ".current-llm-prompt" ]; then
    changes=$(git status --porcelain 2>/dev/null | wc -l)
    if [ "$changes" -gt 0 ]; then
        echo ""
        echo "💡 Tip: You have uncommitted changes. To commit with the LLM prompt:"
        echo "   git add ."
        echo "   git commit"
        echo ""
        echo "The prompt will be automatically included in your commit message."
    fi
fi