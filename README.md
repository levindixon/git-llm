# git-llm

🔬 Research project exploring the intersection of AI-assisted development and version control. How should we preserve the context of LLM interactions that generate code? This repository investigates various approaches to capturing, storing, and retrieving AI prompts within Git workflows.

## 🎯 Problem Statement

When using LLMs to write code, the prompts that guide the AI contain valuable context about:
- **Why** changes were made (not just what)
- Business requirements and constraints
- Design decisions and trade-offs
- The iterative refinement process

This context is typically lost after the code is generated, leaving future developers without crucial understanding of the original intent.

## 💡 Solution

This project researches and implements various approaches to capture, store, and retrieve LLM prompts as part of the Git workflow, making them a permanent part of your project's history.

## 📚 Repository Structure

```
git-llm/
├── capture-prompts-evaluation.md  # Synthesis and recommendations
├── prompt-capture-design.md       # Technical implementation approaches
├── ux-design-overview.md         # User experience design
├── implementation-guide.md        # Step-by-step implementation
├── quick-reference.md            # Feature comparison matrix
├── workflows/                    # Detailed workflow mockups
│   ├── ide-integration-workflow.md
│   ├── cli-wrapper-workflow.md
│   ├── web-interface-workflow.md
│   ├── mobile-companion-workflow.md
│   └── conversation-aggregation-workflow.md
├── examples/                     # Working implementations
│   ├── git-hooks/               # Git hook implementations
│   │   ├── prepare-commit-msg   # Auto-add prompts to commits
│   │   └── commit-msg          # Validate and store prompts
│   ├── scripts/
│   │   └── git-llm             # Comprehensive CLI tool
│   ├── python/
│   │   └── prompt_manager.py   # Python implementation
│   ├── integration/
│   │   └── llm-wrapper.sh      # Wrapper for any LLM CLI
│   └── prompt-formats/
│       └── prompt-schema.json  # Standardized metadata schema
└── README.md                   # This file
```

## Quick Start

1. **Initialize prompt tracking in your repository:**
   ```bash
   ./examples/scripts/git-llm init
   ```

2. **Add a prompt for your next commit:**
   ```bash
   ./examples/scripts/git-llm add "Implement user authentication with JWT"
   ```

3. **Make your code changes and commit:**
   ```bash
   git add .
   git commit -m "feat: add JWT authentication"
   ```

   The prompt will be automatically included in your commit message.

4. **View prompts:**
   ```bash
   ./examples/scripts/git-llm show HEAD
   ./examples/scripts/git-llm list
   ```

## Implementation Approaches

The design document (`prompt-capture-design.md`) covers five approaches:

1. **Git Trailers** - Store prompts in commit messages
2. **Git Notes** - Attach prompts as mutable metadata
3. **Parallel Directory** - Maintain `.prompts/` directory
4. **Git Hooks** - Automatic capture during commit
5. **Hybrid Approach** - Combine multiple methods

## Example Usage

### Using Git Trailers (Simple)

```bash
git commit -m "feat: add authentication

LLM-Prompt: Create JWT-based auth system with refresh tokens
LLM-Model: claude-3-opus-20240229"
```

### Using the Python Implementation

```python
from prompt_manager import GitLLMPromptManager

manager = GitLLMPromptManager()
manager.init()
manager.add_prompt("Implement OAuth2 integration", model="gpt-4")
```

### Using the LLM Wrapper

```bash
# Set up the wrapper
export LLM_TOOL=claude
export PROMPT_CAPTURE_ENABLED=true

# Use your LLM tool - prompt is automatically captured
./examples/integration/llm-wrapper.sh "Refactor the authentication module for better security"
```

## Features

- Multiple storage backends (trailers, notes, files)
- Automatic prompt capture via Git hooks
- Search and export functionality
- Support for rich metadata (model, parameters, context)
- Integration with existing LLM tools
- Validation and schema support

## 🏆 Key Benefits

1. **Knowledge Transfer**: New team members understand the "why" behind code changes
2. **Living Documentation**: Requirements captured at implementation time
3. **Team Learning**: Build collective knowledge of effective AI usage patterns
4. **Debugging Context**: Original intent helps fix issues correctly
5. **Compliance & Audit**: Clear trail of AI-assisted development

## 🚀 Getting Started

### Option 1: Start with the CLI Tool (Recommended)
1. Copy `examples/scripts/git-llm` to your PATH
2. Run `git-llm init` in your repository
3. Use `git-llm add "your prompt"` before commits
4. View history with `git-llm log`

### Option 2: Use Git Hooks
1. Copy hooks from `examples/git-hooks/` to `.git/hooks/`
2. Set `PROMPT_FILE` environment variable before commits
3. Prompts automatically included in commit messages

### Option 3: Integrate with Your Workflow
1. Review the [Implementation Guide](implementation-guide.md)
2. Choose an approach from the [Technical Design](prompt-capture-design.md)
3. Adapt examples to your specific needs

## 📖 Documentation

- **[Evaluation & Recommendations](capture-prompts-evaluation.md)** - Start here for the big picture
- **[Technical Design](prompt-capture-design.md)** - Deep dive into implementation approaches
- **[UX Design](ux-design-overview.md)** - User interaction patterns and workflows
- **[Implementation Guide](implementation-guide.md)** - Step-by-step implementation instructions
- **[Quick Reference](quick-reference.md)** - Feature comparison and decision matrix

## 🔮 Future Vision

This project envisions a future where:
- Every AI-assisted code change preserves its full context
- Teams learn from collective prompt patterns
- Code reviews include prompt evaluation
- Debugging starts with understanding original intent
- AI development practices are transparent and auditable

## 🤝 Contributing

This is an active research project. Contributions welcome:
- Test implementations and provide feedback
- Share use cases and requirements
- Contribute alternative approaches
- Help build the prompt pattern library

## 📝 License

This is a research project. All examples and documentation are provided as-is for educational and implementation purposes. Feel free to adapt for your needs.