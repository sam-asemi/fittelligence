# FitTelligence - Project Layout & Agent Relationships

## 📁 Complete File Structure

```
fittelligence-1/
│
├── 📄 demo.py                              # Main demo with interactive input
├── 📄 requirements.txt                     # Python dependencies
├── 📄 .gitignore                           # Git ignore rules
├── 📄 LICENSE                              # MIT License
│
├── 📚 Documentation/
│   ├── README.md                           # Main documentation
│   ├── SUBMISSION_WRITEUP.md              # Kaggle submission document
│   ├── KAGGLE_SUBMISSION.md               # Technical details
│   ├── QUICK_START.md                     # Quick start guide
│   ├── ADK_UI_GUIDE.md                    # ADK Web UI instructions
│   ├── SUBMISSION_SUMMARY.md              # Submission checklist
│   ├── GITHUB_FILES.md                    # GitHub file list
│   ├── PROJECT_ARCHITECTURE.md            # Architecture details
│   └── PROJECT_LAYOUT.md                  # This file
│
├── 🤖 Agents (5 specialized agents)
│   │
│   ├── 📁 reception_agent/                 # Agent 1
│   │   ├── __init__.py
│   │   └── agent.py
│   │       • Collects client information
│   │       • Health & fitness background
│   │       • Goals & preferences
│   │
│   ├── 📁 body_scanner_agent/              # Agent 2
│   │   ├── __init__.py
│   │   └── agent.py
│   │       • Analyzes body posture
│   │       • Movement patterns
│   │       • Mobility assessments
│   │
│   ├── 📁 pt_agent/                        # Agent 3
│   │   ├── __init__.py
│   │   └── agent.py
│   │       • Creates training plans
│   │       • Exercise programming
│   │       • Progression planning
│   │
│   ├── 📁 nutrition_agent/                 # Agent 4
│   │   ├── __init__.py
│   │   └── agent.py
│   │       • Creates nutrition plans
│   │       • Meal planning
│   │       • Macronutrient targets
│   │
│   └── 📁 head_coach_agent/                # Agent 5 (Coordinator)
│       ├── __init__.py
│       └── agent.py
│           • Coordinates all agents
│           • Uses A2A communication tools
│           • Integrates final program
│
└── 🔗 shared/
    ├── __init__.py
    └── agent_communication.py              # A2A Protocol implementation
        • get_client_information_from_reception()
        • get_body_analysis_from_scanner()
        • get_training_plan_from_pt_agent()
        • get_nutrition_plan_from_nutrition_agent()
```

---

## 🔄 Agent Relationship Diagram

```
                    ┌─────────────────────────┐
                    │   USER / CLIENT         │
                    └───────────┬─────────────┘
                                │
                                │ Provides input
                                │
                    ┌───────────▼─────────────┐
                    │      demo.py            │
                    │   (Orchestrator)        │
                    │                         │
                    │ • Interactive input     │
                    │ • Session management    │
                    │ • Sequential execution  │
                    └───────────┬─────────────┘
                                │
                    ┌───────────┴───────────┐
                    │                       │
                    │   Sequential Flow     │
                    │                       │
                    ▼                       ▼

    ┌──────────────────────────┐
    │  1. Reception Agent      │
    │  ─────────────────────   │
    │  Input:  User data       │
    │  Output: Client profile  │
    │                          │
    │  Tools:                  │
    │  • Google Search         │
    │  • PreloadMemoryTool     │
    └───────────┬──────────────┘
                │
                │ Context: Client intake data
                │
    ┌───────────▼──────────────────────────┐
    │  2. Body Scanner Agent               │
    │  ────────────────────────────        │
    │  Input:  Client profile              │
    │  Output: Body analysis               │
    │                                     │
    │  Tools:                             │
    │  • Google Search                    │
    │  • PreloadMemoryTool                │
    │  • Context from Reception           │
    └───────────┬──────────────────────────┘
                │
                │ Context: Intake + Body analysis
                │
    ┌───────────▼──────────────────────────┐
    │  3. PT Agent                         │
    │  ────────────────────────            │
    │  Input:  Intake + Body analysis      │
    │  Output: Training plan               │
    │                                     │
    │  Tools:                             │
    │  • Google Search                    │
    │  • PreloadMemoryTool                │
    │  • Context from previous agents     │
    └───────────┬──────────────────────────┘
                │
                │ Context: Intake + Body + Training
                │
    ┌───────────▼──────────────────────────┐
    │  4. Nutrition Agent                  │
    │  ────────────────────────            │
    │  Input:  All previous data           │
    │  Output: Nutrition plan              │
    │                                     │
    │  Tools:                             │
    │  • Google Search                    │
    │  • PreloadMemoryTool                │
    │  • Full context                     │
    └───────────┬──────────────────────────┘
                │
                │ Context: ALL information
                │
    ┌───────────▼──────────────────────────┐
    │  5. Head Coach Agent                 │
    │  ─────────────────────────────       │
    │  Input:  Everything                  │
    │  Output: Integrated program          │
    │                                     │
    │  Tools:                             │
    │  • Google Search                    │
    │  • PreloadMemoryTool                │
    │  • A2A Communication Tools:         │
    │    ├─ get_client_information()      │
    │    ├─ get_body_analysis()           │
    │    ├─ get_training_plan()           │
    │    └─ get_nutrition_plan()          │
    │                                     │
    │  Can call other agents via tools    │
    └───────────┬──────────────────────────┘
                │
                ▼
        ┌───────────────────┐
        │  FINAL PROGRAM    │
        │                   │
        │  • Training       │
        │  • Nutrition      │
        │  • Integrated     │
        └───────────────────┘
```

---

## 🔗 A2A Communication Structure

```
head_coach_agent
    │
    │ Uses custom tools from shared/agent_communication.py
    │
    ├─► get_client_information_from_reception()
    │   └─► Calls: reception_agent
    │
    ├─► get_body_analysis_from_scanner()
    │   └─► Calls: body_scanner_agent
    │
    ├─► get_training_plan_from_pt_agent()
    │   └─► Calls: pt_agent
    │
    └─► get_nutrition_plan_from_nutrition_agent()
        └─► Calls: nutrition_agent

shared/agent_communication.py
    └─► Contains all A2A communication functions
```

---

## 🛠️ Tool Distribution

```
┌─────────────────────────────────────────────────┐
│  BUILT-IN TOOLS (All Agents)                   │
├─────────────────────────────────────────────────┤
│  ✓ Google Search                                │
│  ✓ PreloadMemoryTool                            │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│  CUSTOM TOOLS (Head Coach Only)                │
├─────────────────────────────────────────────────┤
│  ✓ get_client_information_from_reception()      │
│  ✓ get_body_analysis_from_scanner()             │
│  ✓ get_training_plan_from_pt_agent()            │
│  ✓ get_nutrition_plan_from_nutrition_agent()    │
└─────────────────────────────────────────────────┘
```

---

## 💾 Session & Memory Architecture

```
InMemorySessionService (Shared Instance)
    │
    ├─► Reception Agent Session
    │   └─ Key: (user_id, session_id, "reception_agent")
    │
    ├─► Body Scanner Agent Session
    │   └─ Key: (user_id, session_id, "body_scanner_agent")
    │
    ├─► PT Agent Session
    │   └─ Key: (user_id, session_id, "pt_agent")
    │
    ├─► Nutrition Agent Session
    │   └─ Key: (user_id, session_id, "nutrition_agent")
    │
    └─► Head Coach Agent Session
        └─ Key: (user_id, session_id, "head_coach_agent")

PreloadMemoryTool (In All Agents)
    └─► Enables long-term memory across sessions
```

---

## 📊 Information Flow Summary

```
User Input
    │
    ├─► Reception Agent
    │       └─► Client Profile
    │
    ├─► Body Scanner Agent (receives: Client Profile)
    │       └─► Body Analysis
    │
    ├─► PT Agent (receives: Client Profile + Body Analysis)
    │       └─► Training Plan
    │
    ├─► Nutrition Agent (receives: All previous data)
    │       └─► Nutrition Plan
    │
    └─► Head Coach Agent (receives: EVERYTHING)
            └─► Final Integrated Program
```

---

## 🎯 Key Design Principles

1. **Sequential Flow**: Each agent builds on previous agents' work
2. **Context Passing**: Information flows forward through the chain
3. **Specialization**: Each agent has a specific domain expertise
4. **Coordination**: Head coach agent coordinates and integrates
5. **Tool Sharing**: Built-in tools available to all; custom tools for coordination
6. **Session Isolation**: Each agent has its own session but shares context
7. **Memory Integration**: All agents can remember past interactions

---

**This architecture demonstrates a clean, scalable multi-agent system with proper separation of concerns and sequential information flow.**

