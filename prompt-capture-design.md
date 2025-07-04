# Technical Approaches for Capturing and Storing LLM Prompts with Git Commits

## Overview

This document explores five different technical approaches for capturing and storing LLM prompts alongside Git commits, maintaining Git compatibility while ensuring prompts are easily accessible.

## Approach 1: Extended Commit Messages with Git Trailers

### Implementation

Use Git trailers (key-value pairs) in commit messages to store prompts:

```
feat: implement user authentication

Add JWT-based authentication system with refresh tokens

LLM-Prompt: Create a secure authentication system using JWT tokens with
  refresh token support. Include middleware for protecting routes and
  handle token expiration gracefully.
LLM-Model: claude-3-opus-20240229
LLM-Timestamp: 2024-07-03T10:30:00Z
```

### Technical Details

```bash
# Add prompt using --trailer flag (Git 2.32+)
git commit --trailer "LLM-Prompt:Create authentication system..." \
           --trailer "LLM-Model:claude-3-opus-20240229"

# Parse trailers
git log --format="%(trailers:key=LLM-Prompt)"
```

### Pros
- Native Git support (no additional tools required)
- Immutable and version-controlled with commits
- Visible in standard git log
- Works with all Git hosting platforms
- Can be enforced via commit-msg hooks

### Cons
- Limited to text format
- Makes commit messages longer
- Cannot be modified after commit
- May clutter commit history for simple prompts
- Character limits on some platforms

## Approach 2: Git Notes for Prompt Storage

### Implementation

Attach prompts as Git notes to commits:

```bash
# Add note to latest commit
git notes add -m '{
  "prompt": "Create a secure authentication system...",
  "model": "claude-3-opus-20240229",
  "timestamp": "2024-07-03T10:30:00Z",
  "temperature": 0.7,
  "max_tokens": 4000
}'

# Or add to specific commit
git notes add <commit-hash> -m '...'
```

### Technical Details

```bash
# Create custom notes ref for prompts
git notes --ref=llm-prompts add -m '...'

# View notes
git log --show-notes=llm-prompts

# Push/pull notes
git push origin refs/notes/llm-prompts
git fetch origin refs/notes/llm-prompts:refs/notes/llm-prompts
```

### Pros
- Mutable (can be updated after commit)
- Doesn't affect commit SHA
- Supports any data format (JSON, YAML, etc.)
- Can store large prompts
- Version controlled separately

### Cons
- Not displayed by default in git log
- Requires manual push/pull
- Poor support in Git hosting platforms (GitHub doesn't display)
- Easy to lose if not explicitly synchronized
- Additional complexity for team workflows

## Approach 3: Parallel .prompts Directory

### Implementation

Create a `.prompts/` directory that mirrors commit structure:

```
.prompts/
├── by-hash/
│   ├── abc123.json
│   ├── def456.json
│   └── ghi789.json
├── by-date/
│   └── 2024/
│       └── 07/
│           └── 03/
│               └── 10-30-00-abc123.json
└── index.json
```

### Technical Details

```json
// .prompts/by-hash/abc123.json
{
  "commit": "abc123...",
  "prompt": "Create a secure authentication system...",
  "model": "claude-3-opus-20240229",
  "timestamp": "2024-07-03T10:30:00Z",
  "context": {
    "files_changed": ["src/auth.js", "src/middleware.js"],
    "branch": "feature/authentication"
  },
  "response_metadata": {
    "tokens_used": 3500,
    "completion_time": 45.2
  }
}
```

### Pros
- Rich metadata support
- Easy to query and analyze
- Can store multiple prompts per commit
- Supports versioning of prompt storage format
- Can include additional context (diffs, file lists)

### Cons
- Requires manual maintenance
- Can get out of sync with commits
- Takes up repository space
- Need to handle merge conflicts
- Requires custom tooling for access

## Approach 4: Git Hooks for Automatic Capture

### Implementation

Use `prepare-commit-msg` and `commit-msg` hooks:

```bash
#!/bin/bash
# .git/hooks/prepare-commit-msg

# Check for prompt in environment or file
if [ -f ".current-prompt" ]; then
    prompt=$(cat .current-prompt)
    echo "" >> "$1"
    echo "LLM-Prompt: $prompt" >> "$1"
    rm .current-prompt
fi
```

```bash
#!/bin/bash
# .git/hooks/commit-msg

# Validate prompt format and store in .prompts/
commit_hash=$(git rev-parse HEAD)
prompt=$(grep "^LLM-Prompt:" "$1" | cut -d: -f2-)

if [ ! -z "$prompt" ]; then
    mkdir -p .prompts/by-hash
    echo "{
        \"prompt\": \"$prompt\",
        \"timestamp\": \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\"
    }" > ".prompts/by-hash/${commit_hash}.json"
fi
```

### Integration with LLM tools:

```bash
# Wrapper script for LLM CLI tools
llm-commit() {
    # Save prompt for next commit
    echo "$1" > .current-prompt
    
    # Execute LLM command
    llm-cli "$1"
    
    # Create commit with captured prompt
    git add .
    git commit
}
```

### Pros
- Automatic capture
- Integrates with existing workflow
- Can validate prompt format
- Works with any Git client
- Can trigger additional automation

### Cons
- Requires hook setup on each clone
- Platform-specific scripts
- Can't capture prompts retroactively
- May interfere with other hooks
- Security concerns with automatic execution

## Approach 5: Hybrid Storage Format

### Implementation

Combine multiple approaches for maximum flexibility:

```yaml
# .llm-prompts.yml
version: 1.0
storage:
  inline: true      # Store short prompts in commit messages
  notes: true       # Store full prompts in git notes
  directory: true   # Maintain .prompts/ for queries

rules:
  - if: prompt.length < 500
    use: commit-trailer
  - if: prompt.length >= 500
    use: git-notes
  - always: 
    backup-to: .prompts/

metadata:
  capture:
    - prompt
    - model
    - timestamp
    - context
    - response_summary
```

### CLI Tool Example:

```bash
# git-llm command
git llm add "Create authentication system"
git llm show <commit>
git llm search "authentication"
git llm export --format=json > prompts-export.json
```

### Pros
- Best of all approaches
- Flexible storage based on needs
- Standardized tooling
- Can evolve over time
- Supports team workflows

### Cons
- Most complex to implement
- Requires custom tooling
- May have synchronization issues
- Learning curve for teams
- Maintenance overhead

## Recommended Implementation Strategy

### Phase 1: Start Simple
1. Use Git trailers for basic prompt storage
2. Implement commit-msg hook for validation
3. Create simple parsing scripts

### Phase 2: Add Persistence
1. Implement .prompts/ directory structure
2. Add Git hooks for automatic capture
3. Build query tools

### Phase 3: Advanced Features
1. Add Git notes for large prompts
2. Implement hybrid storage rules
3. Create comprehensive CLI tool

## Storage Format Recommendations

### JSON (Recommended for structured data)
```json
{
  "version": "1.0",
  "prompt": {
    "text": "...",
    "type": "feature|fix|refactor|docs"
  },
  "llm": {
    "model": "...",
    "parameters": {}
  },
  "metadata": {
    "timestamp": "...",
    "author": "..."
  }
}
```

### YAML (Better for human editing)
```yaml
version: 1.0
prompt:
  text: |
    Create a secure authentication system
    with JWT tokens and refresh support
  type: feature
llm:
  model: claude-3-opus
  temperature: 0.7
```

### Markdown (Best for documentation)
```markdown
## Prompt

Create a secure authentication system...

### Metadata
- Model: claude-3-opus
- Date: 2024-07-03
- Type: feature

### Context
Files affected: auth.js, middleware.js
```

## Conclusion

The best approach depends on your specific needs:

- **For simplicity**: Use Git trailers
- **For flexibility**: Use Git notes
- **For rich queries**: Use .prompts/ directory
- **For automation**: Use Git hooks
- **For completeness**: Use hybrid approach

Consider starting with Git trailers and hooks, then expanding to more sophisticated solutions as needs grow.