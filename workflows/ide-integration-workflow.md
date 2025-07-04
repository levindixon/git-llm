# IDE Integration Workflow

## VS Code Extension: "Prompt Keeper"

### Initial Setup
```
1. Install "Prompt Keeper" extension from marketplace
2. Configure storage location (local/cloud)
3. Set capture preferences:
   [ ] Auto-capture all prompts
   [x] Require confirmation for sensitive code
   [x] Include generated code in capture
   [ ] Capture failed/error responses
```

### Active Capture Flow

```
Developer writes prompt in AI assistant panel:
┌─────────────────────────────────────┐
│ AI Assistant                    [-][x]│
├─────────────────────────────────────┤
│ > Create a React component that      │
│   displays user profile with avatar  │
│   and editable fields               │
│                                     │
│ [Send] [📌 Save Prompt]             │
└─────────────────────────────────────┘
                 ↓
         User clicks "Save Prompt"
                 ↓
┌─────────────────────────────────────┐
│ Save Prompt                         │
├─────────────────────────────────────┤
│ Title: [React Profile Component    ]│
│                                     │
│ Tags: [react] [component] [ui]  [+] │
│                                     │
│ Category: [Frontend Components   ▼] │
│                                     │
│ Notes: ________________________    │
│        ________________________    │
│                                     │
│ [x] Include generated code          │
│ [ ] Mark as template               │
│                                     │
│ [Cancel]              [Save]        │
└─────────────────────────────────────┘
```

### Passive Capture Flow

```
Background capture with notification:
┌─────────────────────────────────────┐
│ Code Editor                         │
│                                     │
│ // UserProfile.jsx                  │
│ import React from 'react';          │
│ ...                                 │
│                                     │
│ ┌─────────────────────────┐         │
│ │ 🔔 Prompt auto-captured │         │
│ │ View | Dismiss          │         │
│ └─────────────────────────┘         │
└─────────────────────────────────────┘
```

### Prompt History Sidebar

```
┌──────────────────────┐
│ PROMPT HISTORY       │
├──────────────────────┤
│ 🔍 Search...         │
├──────────────────────┤
│ Today                │
│ ├─ React Profile     │
│ │  #react #component │
│ │  2:34 PM          │
│ ├─ API Integration   │
│ │  #backend #api     │
│ │  11:20 AM         │
│ │                    │
│ Yesterday            │
│ ├─ Database Schema   │
│ │  #sql #postgres    │
│ └─ Auth Middleware   │
│    #security #auth   │
│                      │
│ [Export] [Settings]  │
└──────────────────────┘
```

### Code Annotation View

```
┌─────────────────────────────────────────────┐
│ UserProfile.jsx                             │
├─────────────────────────────────────────────┤
│ 1  import React, { useState } from 'react'; │
│ 2  import './UserProfile.css';              │
│ 3                                           │
│ 4  // 💬 Generated from prompt:             │
│ 5  // "Create a React component that        │
│ 6  //  displays user profile with avatar"   │
│ 7  // Captured: 2024-01-15 14:34           │
│ 8  // [View Full Prompt]                    │
│ 9                                           │
│ 10 const UserProfile = ({ user }) => {      │
│ 11   const [isEditing, setIsEditing] =     │
│      useState(false);                       │
└─────────────────────────────────────────────┘
```