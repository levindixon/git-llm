# Conversation Aggregation Workflow

## Automatic Multi-Turn Conversation Tracking

### Conversation Detection & Grouping

```
┌────────────────────────────────────────────────────────────┐
│ Active Conversation: "Building Authentication System"      │
├────────────────────────────────────────────────────────────┤
│                                                            │
│ 🔄 Conversation Timeline (Started: 10:15 AM)               │
│                                                            │
│ Turn 1 (10:15 AM)                                         │
│ ┌──────────────────────────────────────────────────────┐ │
│ │ 👤 "Create a user authentication system with JWT"     │ │
│ │ 🤖 Generated: auth.js, jwt-config.js                  │ │
│ └──────────────────────────────────────────────────────┘ │
│                    ↓                                       │
│ Turn 2 (10:22 AM)                                         │
│ ┌──────────────────────────────────────────────────────┐ │
│ │ 👤 "Add password reset functionality"                 │ │
│ │ 🤖 Generated: reset-password.js, email-template.html  │ │
│ └──────────────────────────────────────────────────────┘ │
│                    ↓                                       │
│ Turn 3 (10:28 AM) - Current                              │
│ ┌──────────────────────────────────────────────────────┐ │
│ │ 👤 "Implement rate limiting for auth endpoints"       │ │
│ │ 🤖 Generating...                                      │ │
│ └──────────────────────────────────────────────────────┘ │
│                                                            │
│ Context Maintained: ✅ Same project, Related files         │
│ Auto-save: ON | Conversation will close after 30min idle  │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

### Intelligent Context Detection

```
┌────────────────────────────────────────────────────────────┐
│ 🧠 Context Analyzer                                        │
├────────────────────────────────────────────────────────────┤
│                                                            │
│ Current Context:                                           │
│ • Project: E-commerce Platform                            │
│ • Module: Authentication                                   │
│ • Files: auth/*, middleware/*                             │
│ • Language: JavaScript/Node.js                             │
│                                                            │
│ Related Prompts Detected:                                  │
│ ┌──────────────────────────────────────────────────────┐ │
│ │ ⚡ High Relevance (Same feature)                      │ │
│ │ • "Create login endpoint" (5 min ago)                │ │
│ │ • "Add OAuth integration" (12 min ago)               │ │
│ │                                                       │ │
│ │ 🔗 Medium Relevance (Same module)                     │ │
│ │ • "User profile management" (1 hour ago)             │ │
│ │ • "Session handling" (2 hours ago)                   │ │
│ │                                                       │ │
│ │ 💡 Suggested Grouping: "Auth System Implementation"   │ │
│ └──────────────────────────────────────────────────────┘ │
│                                                            │
│ [Accept Grouping] [Modify] [Create New Conversation]       │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

### Conversation Summary View

```
┌────────────────────────────────────────────────────────────┐
│ Conversation: "Building Authentication System"             │
│ Duration: 45 minutes | Turns: 6 | Status: Completed ✅     │
├────────────────────────────────────────────────────────────┤
│                                                            │
│ 📊 Summary                                                 │
│ ┌──────────────────────────────────────────────────────┐ │
│ │ Goal: Implement complete authentication system        │ │
│ │                                                       │ │
│ │ Key Components Built:                                 │ │
│ │ • JWT-based authentication                           │ │
│ │ • Password reset flow                                │ │
│ │ • Rate limiting middleware                           │ │
│ │ • OAuth2 integration (Google, GitHub)                │ │
│ │                                                       │ │
│ │ Files Created: 12                                     │ │
│ │ Tests Written: 8                                      │ │
│ │ Success Rate: 100%                                    │ │
│ └──────────────────────────────────────────────────────┘ │
│                                                            │
│ 💬 Conversation Flow                                       │
│ ┌──────────────────────────────────────────────────────┐ │
│ │ 1. Initial auth setup → 2. Password management →     │ │
│ │ 3. Rate limiting → 4. OAuth setup → 5. Testing →     │ │
│ │ 6. Documentation                                      │ │
│ └──────────────────────────────────────────────────────┘ │
│                                                            │
│ [Export Thread] [View Code] [Generate Docs] [Archive]      │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

### Auto-Aggregation Settings

```
┌────────────────────────────────────────────────────────────┐
│ ⚙️ Conversation Aggregation Settings                       │
├────────────────────────────────────────────────────────────┤
│                                                            │
│ Grouping Rules:                                            │
│ ┌──────────────────────────────────────────────────────┐ │
│ │ ☑️ Group by time proximity (< 30 min)                 │ │
│ │ ☑️ Group by file context (same directory)             │ │
│ │ ☑️ Group by semantic similarity                       │ │
│ │ ☐ Group by explicit tags only                        │ │
│ └──────────────────────────────────────────────────────┘ │
│                                                            │
│ Context Detection:                                         │
│ • Idle timeout: [30 minutes ▼]                            │
│ • Max conversation length: [2 hours ▼]                    │
│ • Include refactoring prompts: [Yes ▼]                    │
│                                                            │
│ Auto-Summary:                                              │
│ ☑️ Generate summary after conversation ends                │
│ ☑️ Extract key decisions and rationale                    │
│ ☑️ Create relationship diagram for complex flows           │
│                                                            │
│ Storage:                                                   │
│ • Keep conversations for: [90 days ▼]                     │
│ • Archive location: [.prompts/conversations/]             │
│                                                            │
│ [Save Settings] [Reset to Defaults]                        │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

### Conversation Export Format

```
┌────────────────────────────────────────────────────────────┐
│ Export Conversation                                        │
├────────────────────────────────────────────────────────────┤
│                                                            │
│ Format Options:                                            │
│                                                            │
│ 📝 Markdown (Recommended)                                  │
│ ┌──────────────────────────────────────────────────────┐ │
│ │ # Authentication System Implementation                │ │
│ │ Date: 2024-01-15 | Duration: 45 minutes             │ │
│ │                                                       │ │
│ │ ## Conversation Flow                                  │ │
│ │ ### Turn 1: Basic JWT Setup                          │ │
│ │ **Prompt**: Create a user authentication...          │ │
│ │ **Result**: Generated auth.js with...                │ │
│ │ ```javascript                                         │ │
│ │ // Generated code here                                │ │
│ │ ```                                                   │ │
│ └──────────────────────────────────────────────────────┘ │
│                                                            │
│ 🔧 JSON (For tooling integration)                          │
│ 📊 CSV (Prompts only)                                      │
│ 📦 Full Archive (ZIP with code + prompts)                  │
│                                                            │
│ Include:                                                   │
│ ☑️ All prompts and responses                               │
│ ☑️ Generated code files                                    │
│ ☑️ Timestamp for each turn                                 │
│ ☐ Error messages and retries                              │
│ ☑️ Final working solution                                  │
│                                                            │
│ [Cancel]                               [Export]            │
│                                                            │
└────────────────────────────────────────────────────────────┘
```