# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a research project exploring methods to capture and preserve LLM prompts alongside Git commits, creating "AI Development Records". The project provides multiple implementation approaches and examples in different languages.

## Common Development Tasks

### Testing Example Implementations

1. **Test the Bash CLI tool:**
   ```bash
   chmod +x examples/scripts/git-llm
   ./examples/scripts/git-llm init
   ./examples/scripts/git-llm add "Test prompt"
   ./examples/scripts/git-llm list
   ```

2. **Test Python implementation:**
   ```bash
   python3 examples/python/prompt_manager.py --help
   python3 examples/python/prompt_manager.py init
   python3 examples/python/prompt_manager.py add "Test prompt"
   ```

3. **Test Git hooks:**
   ```bash
   cp examples/git-hooks/prepare-commit-msg .git/hooks/
   cp examples/git-hooks/commit-msg .git/hooks/
   chmod +x .git/hooks/*
   echo "Test prompt" > .current-llm-prompt
   git commit -m "Test commit"
   ```

### Validation Commands

When modifying shell scripts:
```bash
shellcheck examples/scripts/git-llm
shellcheck examples/integration/llm-wrapper.sh
```

When modifying Python code:
```bash
python3 -m py_compile examples/python/prompt_manager.py
```

## Code Architecture

### Storage Approaches
The project implements multiple storage backends that can be used independently or together:

1. **Git Trailers**: Stores prompts directly in commit messages using Git's trailer format
2. **Git Notes**: Attaches prompts as mutable metadata using Git's notes system
3. **Directory Storage**: Maintains prompts in `.prompts/` directory with by-hash and by-date organization
4. **Hybrid**: Combines multiple approaches for redundancy and flexibility

### Key Implementation Files

- `examples/scripts/git-llm`: Main Bash implementation - comprehensive CLI tool with all features
- `examples/python/prompt_manager.py`: Python class-based implementation (`GitLLMPromptManager`)
- `examples/git-hooks/`: Automatic prompt capture via Git hooks
- `examples/integration/llm-wrapper.sh`: Wrapper for any LLM CLI tool
- `examples/prompt-formats/prompt-schema.json`: JSON schema defining prompt metadata structure

### Data Flow

1. **Capture**: Prompts are captured via CLI commands, environment variables, or files
2. **Storage**: Prompts are stored using the configured backend(s)
3. **Association**: Prompts are linked to Git commits using commit hash
4. **Retrieval**: Prompts can be retrieved by commit, date, or search pattern

### Integration Points

- Environment variables: `PROMPT_FILE`, `LLM_PROMPT`, `LLM_MODEL`
- Git hooks: `prepare-commit-msg`, `commit-msg`
- CLI commands: Extends Git with `git llm` subcommand
- File-based: `.current-llm-prompt` for pending prompts

## Important Patterns

- All timestamps use UTC with ISO 8601 format
- Commit hashes are stored as full 40-character strings
- JSON files use 2-space indentation
- Shell scripts follow strict error handling with `set -e`
- Python code targets Python 3.6+ with standard library only