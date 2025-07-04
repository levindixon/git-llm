# Mobile Companion App Workflow

## "PromptKeeper" Mobile App

### Quick Capture Screen

```
┌─────────────────────────┐
│ 9:41 AM        🔋 92%  │
├─────────────────────────┤
│                         │
│    PromptKeeper        │
│                         │
│ ┌─────────────────────┐ │
│ │                     │ │
│ │    📝 Quick Save    │ │
│ │                     │ │
│ │  Tap to capture a   │ │
│ │  voice prompt       │ │
│ │                     │ │
│ │      [🎤]           │ │
│ │                     │ │
│ └─────────────────────┘ │
│                         │
│ Recent Captures         │
│ ┌─────────────────────┐ │
│ │ "Create auth flow"  │ │
│ │ 2 min ago          │ │
│ ├─────────────────────┤ │
│ │ "Fix mobile layout" │ │
│ │ 1 hour ago         │ │
│ └─────────────────────┘ │
│                         │
│ [📚] [🔍] [➕] [⚙️]    │
└─────────────────────────┘
```

### Voice-to-Prompt Flow

```
Step 1: Recording
┌─────────────────────────┐
│                         │
│   Recording Prompt...   │
│                         │
│      ⏺️ 0:08          │
│                         │
│   ████████░░░░░░░░░    │
│                         │
│ "Create a Python script │
│  that monitors system   │
│  resources and sends    │
│  alerts when..."        │
│                         │
│    [⏸️ Pause] [✓ Done]  │
│                         │
└─────────────────────────┘

Step 2: Review & Tag
┌─────────────────────────┐
│ Review Prompt          │
├─────────────────────────┤
│                         │
│ Transcribed:            │
│ ┌─────────────────────┐ │
│ │Create a Python       │ │
│ │script that monitors  │ │
│ │system resources and  │ │
│ │sends alerts when     │ │
│ │CPU or memory usage   │ │
│ │exceeds 80%           │ │
│ └─────────────────────┘ │
│                         │
│ Add Tags:               │
│ [python] [monitoring]   │
│ [+ Add tag]             │
│                         │
│ Project: [DevOps ▼]     │
│                         │
│ [Cancel]    [Save]      │
└─────────────────────────┘
```

### Desktop Sync Notification

```
┌─────────────────────────┐
│ 🔔 New from Mobile      │
├─────────────────────────┤
│                         │
│ 3 new prompts ready     │
│ to sync                 │
│                         │
│ • System monitoring     │
│ • Database backup       │
│ • API rate limiting     │
│                         │
│ [Sync Now] [Later]      │
└─────────────────────────┘
```

### Browse & Search View

```
┌─────────────────────────┐
│ 🔍 Search              │
├─────────────────────────┤
│                         │
│ Filter: [This Week ▼]   │
│ Tags: [All ▼]           │
│                         │
│ Results (18)            │
│ ┌─────────────────────┐ │
│ │ React Component      │ │
│ │ Gallery              │ │
│ │ #react #ui          │ │
│ │ Yesterday • Desktop  │ │
│ │ ─────────────────── │ │
│ │ "Create a React      │ │
│ │ component for..."    │ │
│ │                      │ │
│ │ [View] [Share] [📋]  │ │
│ └─────────────────────┘ │
│ ┌─────────────────────┐ │
│ │ Database Schema      │ │
│ │ #sql #postgres       │ │
│ │ 2 days ago • Mobile  │ │
│ └─────────────────────┘ │
│                         │
└─────────────────────────┘
```

### Share & Export

```
┌─────────────────────────┐
│ Share Prompt           │
├─────────────────────────┤
│                         │
│ Selected: React Gallery │
│                         │
│ Share via:              │
│ ┌─────────────────────┐ │
│ │ 📧 Email            │ │
│ │ 💬 Slack            │ │
│ │ 📱 Messages         │ │
│ │ 🔗 Copy Link        │ │
│ └─────────────────────┘ │
│                         │
│ Export format:          │
│ ○ Markdown             │
│ ● JSON                 │
│ ○ Plain Text           │
│                         │
│ Include:                │
│ ☑️ Generated code       │
│ ☑️ Timestamps           │
│ ☐ Version history      │
│                         │
│ [Cancel]    [Share]     │
└─────────────────────────┘
```