# CLI Wrapper Workflow

## "prompt-capture" CLI Tool

### Installation and Setup

```bash
# Install globally
$ npm install -g prompt-capture

# Initialize in project
$ prompt-capture init
? Where to store prompts? (.prompts)
? Enable auto-capture? (Y/n)
? Integrate with Git? (Y/n)
? Default AI provider? (openai/anthropic/custom)
```

### Basic Usage Flow

```bash
# Wrapped AI interaction
$ prompt-capture ask "Create a Python function to validate email addresses"

┌─────────────────────────────────────────┐
│ 🤖 Generating response...               │
├─────────────────────────────────────────┤
│ def validate_email(email):              │
│     import re                           │
│     pattern = r'^[a-zA-Z0-9._%+-]+@'   │
│     ...                                 │
└─────────────────────────────────────────┤

Save this prompt? (Y/n/e[dit]): Y
✓ Prompt saved to .prompts/2024-01-15-validate-email.md

# Copy to clipboard
$ prompt-capture ask "..." --copy

# Direct file output
$ prompt-capture ask "..." --output utils/email.py
```

### Git Integration Flow

```bash
# Automatic prompt tracking with commits
$ prompt-capture commit -m "Add email validation"

┌─────────────────────────────────────────┐
│ Detected AI-generated files:            │
│ - utils/email.py                        │
│ - tests/test_email.py                   │
│                                         │
│ Found related prompts (2):              │
│ 1. "Create a Python function to..."     │
│ 2. "Write unit tests for email..."      │
│                                         │
│ Include prompts in commit? (Y/n): Y     │
└─────────────────────────────────────────┤

[main abc123] Add email validation
 3 files changed, 45 insertions(+)
 create mode 100644 utils/email.py
 create mode 100644 tests/test_email.py
 create mode 100644 .prompts/email-validation.md
```

### Session Management

```bash
# Start a coding session
$ prompt-capture session start "Feature: User Authentication"

🔴 Recording session: Feature: User Authentication
All prompts will be grouped under this session.

$ prompt-capture ask "Create a login endpoint with JWT"
$ prompt-capture ask "Add password hashing with bcrypt"
$ prompt-capture ask "Implement refresh token logic"

# End session and review
$ prompt-capture session end

┌─────────────────────────────────────────┐
│ Session Summary                         │
├─────────────────────────────────────────┤
│ Feature: User Authentication            │
│ Duration: 45 minutes                    │
│ Prompts: 3                              │
│ Files created: 5                        │
│                                         │
│ Export session? (markdown/json/none): m │
└─────────────────────────────────────────┤

✓ Session exported to docs/auth-session-2024-01-15.md
```

### Prompt Search and Reuse

```bash
# Search captured prompts
$ prompt-capture search "validation"

Found 3 prompts:
1. [2024-01-15] Email validation function
2. [2024-01-10] Form input validation
3. [2024-01-08] API request validation

# Reuse a prompt
$ prompt-capture reuse 1
Loading prompt: "Create a Python function to validate email addresses"
Modify prompt? (y/N): y

# Interactive editor opens
┌─────────────────────────────────────────┐
│ Create a Python function to validate    │
│ email addresses [with support for       │
│ international domains]                  │
└─────────────────────────────────────────┤
```

### Export and Documentation

```bash
# Generate documentation from prompts
$ prompt-capture docs generate

📚 Generating documentation...

Created:
- docs/prompts/README.md (index)
- docs/prompts/backend/api-endpoints.md
- docs/prompts/frontend/components.md
- docs/prompts/testing/test-cases.md

# Export for team sharing
$ prompt-capture export --format json --tag "api"
✓ Exported 12 prompts to prompts-export-api.json

# Stats and analytics
$ prompt-capture stats

📊 Prompt Capture Statistics
├─ Total prompts: 156
├─ This week: 23
├─ Most used tags: #api (34), #react (28), #testing (19)
├─ Success rate: 89%
└─ Avg. session length: 32 minutes
```