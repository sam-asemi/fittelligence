# FitTelligence - Project Architecture & Agent Relationships

## 📐 Project Structure

```
fittelligence-1/
│
├── 📄 demo.py                          # Main demo script (interactive input)
├── 📄 requirements.txt                 # Dependencies
├── 📄 .gitignore                       # Git ignore rules
├── 📄 LICENSE                          # MIT License
│
├── 📁 Documentation/
│   ├── README.md                       # Main documentation
│   ├── SUBMISSION_WRITEUP.md          # Kaggle submission
│   ├── KAGGLE_SUBMISSION.md          # Technical details
│   ├── QUICK_START.md                 # Quick start guide
│   ├── ADK_UI_GUIDE.md                # ADK Web UI guide
│   ├── SUBMISSION_SUMMARY.md          # Submission checklist
│   ├── GITHUB_FILES.md                # GitHub file list
│   └── PROJECT_ARCHITECTURE.md        # This file
│
├── 🤖 reception_agent/
│   ├── __init__.py
│   └── agent.py                       # Agent 1: Client intake
│
├── 📸 body_scanner_agent/
│   ├── __init__.py
│   └── agent.py                       # Agent 2: Body analysis
│
├── 💪 pt_agent/
│   ├── __init__.py
│   └── agent.py                       # Agent 3: Training plans
│
├── 🥗 nutrition_agent/
│   ├── __init__.py
│   └── agent.py                       # Agent 4: Nutrition plans
│
├── 🎯 head_coach_agent/
│   ├── __init__.py
│   └── agent.py                       # Agent 5: Coordinator
│
└── 🔗 shared/
    ├── __init__.py
    └── agent_communication.py         # A2A Protocol tools
```

---

## 🔄 Sequential Agent Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                    FITTELLIGENCE MULTI-AGENT SYSTEM                 │
└─────────────────────────────────────────────────────────────────────┘

    USER INPUT
         │
         ▼
    ┌─────────────────┐
    │  demo.py        │  ◄─── Interactive terminal input
    │  (Orchestrator) │       Collects client information
    └────────┬────────┘
             │
             │ Creates shared session service
             │ Passes context sequentially
             │
             ▼
    ┌─────────────────────────────────────────────────────────────┐
    │                     SEQUENTIAL FLOW                          │
    └─────────────────────────────────────────────────────────────┘
             │
             │
    ┌────────▼────────────────────────────────────────────────────┐
    │  STEP 1: Reception Agent                                    │
    │  ┌──────────────────────────────────────────┐               │
    │  │ • Collects client information            │               │
    │  │ • Health history                         │               │
    │  │ • Fitness background                     │               │
    │  │ • Goals and preferences                  │               │
    │  │                                          │               │
    │  │ Tools: Google Search, PreloadMemoryTool  │               │
    │  └────────────┬─────────────────────────────┘               │
    └───────────────┼─────────────────────────────────────────────┘
                    │
                    │ Context: Client intake data
                    │
    ┌───────────────▼─────────────────────────────────────────────┐
    │  STEP 2: Body Scanner Agent                                 │
    │  ┌──────────────────────────────────────────┐               │
    │  │ • Analyzes body posture                  │               │
    │  │ • Movement pattern assessment            │               │
    │  │ • Mobility test recommendations          │               │
    │  │ • Kinesiology-based analysis             │               │
    │  │                                          │               │
    │  │ Tools: Google Search, PreloadMemoryTool  │               │
    │  │ Context: Intake data                     │               │
    │  └────────────┬─────────────────────────────┘               │
    └───────────────┼─────────────────────────────────────────────┘
                    │
                    │ Context: Intake + Body analysis
                    │
    ┌───────────────▼─────────────────────────────────────────────┐
    │  STEP 3: PT Agent                                           │
    │  ┌──────────────────────────────────────────┐               │
    │  │ • Creates training plan                  │               │
    │  │ • Exercise programming                   │               │
    │  │ • Sets, reps, progression                │               │
    │  │ • Safety considerations                  │               │
    │  │                                          │               │
    │  │ Tools: Google Search, PreloadMemoryTool  │               │
    │  │ Context: Intake + Body analysis          │               │
    │  └────────────┬─────────────────────────────┘               │
    └───────────────┼─────────────────────────────────────────────┘
                    │
                    │ Context: Intake + Body analysis + Training plan
                    │
    ┌───────────────▼─────────────────────────────────────────────┐
    │  STEP 4: Nutrition Agent                                    │
    │  ┌──────────────────────────────────────────┐               │
    │  │ • Creates nutrition plan                 │               │
    │  │ • Meal planning                          │               │
    │  │ • Macronutrient targets                  │               │
    │  │ • Meal timing                            │               │
    │  │                                          │               │
    │  │ Tools: Google Search, PreloadMemoryTool  │               │
    │  │ Context: Intake + Body + Training        │               │
    │  └────────────┬─────────────────────────────┘               │
    └───────────────┼─────────────────────────────────────────────┘
                    │
                    │ Context: ALL previous information
                    │
    ┌───────────────▼─────────────────────────────────────────────┐
    │  STEP 5: Head Coach Agent                                   │
    │  ┌──────────────────────────────────────────┐               │
    │  │ • Coordinates all agents                 │               │
    │  │ • Integrates all information             │               │
    │  │ • Creates final comprehensive program    │               │
    │  │ • Ensures coherence and safety           │               │
    │  │                                          │               │
    │  │ Tools:                                    │               │
    │  │   • Google Search                        │               │
    │  │   • PreloadMemoryTool                    │               │
    │  │   • A2A Communication Tools:             │               │
    │  │     - get_client_information()           │               │
    │  │     - get_body_analysis()                │               │
    │  │     - get_training_plan()                │               │
    │  │     - get_nutrition_plan()               │               │
    │  │                                          │               │
    │  │ Context: EVERYTHING from all agents      │               │
    │  └────────────┬─────────────────────────────┘               │
    └───────────────┼─────────────────────────────────────────────┘
                    │
                    ▼
            ┌───────────────┐
            │  FINAL        │
            │  INTEGRATED   │
            │  PROGRAM      │
            └───────────────┘
```

---

## 🔗 Agent-to-Agent Communication

```
┌─────────────────────────────────────────────────────────────┐
│              A2A PROTOCOL (Agent-to-Agent)                  │
└─────────────────────────────────────────────────────────────┘

    head_coach_agent (Coordinator)
             │
             │ Uses custom tools from shared/agent_communication.py
             │
             ├───► get_client_information_from_reception()
             │     └───► Calls reception_agent
             │
             ├───► get_body_analysis_from_scanner()
             │     └───► Calls body_scanner_agent
             │
             ├───► get_training_plan_from_pt_agent()
             │     └───► Calls pt_agent
             │
             └───► get_nutrition_plan_from_nutrition_agent()
                   └───► Calls nutrition_agent

    shared/agent_communication.py
    └─── Contains all A2A communication functions
```

---

## 🛠️ Tool Integration

Each agent has access to:

```
┌─────────────────────────────────────────┐
│  BUILT-IN TOOLS                         │
├─────────────────────────────────────────┤
│  • Google Search                        │
│    └── Available to all agents          │
│                                         │
│  • PreloadMemoryTool                    │
│    └── Long-term memory for all agents  │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│  CUSTOM TOOLS (A2A Protocol)            │
├─────────────────────────────────────────┤
│  • get_client_information()             │
│  • get_body_analysis()                  │
│  • get_training_plan()                  │
│  • get_nutrition_plan()                 │
│                                         │
│  └── Only in head_coach_agent           │
└─────────────────────────────────────────┘
```

---

## 💾 Session & Memory Management

```
┌─────────────────────────────────────────────────────────────┐
│              SESSION & MEMORY FLOW                          │
└─────────────────────────────────────────────────────────────┘

    InMemorySessionService (Shared Instance)
             │
             ├─── Creates sessions per agent
             │    Key: (user_id, session_id, app_name)
             │
             ├─── Reception Agent Session
             ├─── Body Scanner Agent Session
             ├─── PT Agent Session
             ├─── Nutrition Agent Session
             └─── Head Coach Agent Session

    PreloadMemoryTool (In all agents)
             │
             └─── Enables long-term memory
                  • Remembers past interactions
                  • Recalls client preferences
                  • Maintains context across conversations
```

---

## 📊 Information Flow Diagram

```
┌──────────────────────────────────────────────────────────────┐
│                    INFORMATION FLOW                          │
└──────────────────────────────────────────────────────────────┘

USER INPUT
    │
    ▼
┌────────────────────────┐
│ Reception Agent        │  ◄─── Collects all client info
│                        │
│ Output: Client Profile │
└───────────┬────────────┘
            │
            │ Passes: Client intake data
            ▼
┌────────────────────────┐
│ Body Scanner Agent     │  ◄─── Receives: Client intake
│                        │       Generates: Body analysis
│ Output: Body Analysis  │
└───────────┬────────────┘
            │
            │ Passes: Client intake + Body analysis
            ▼
┌────────────────────────┐
│ PT Agent               │  ◄─── Receives: Intake + Body analysis
│                        │       Generates: Training plan
│ Output: Training Plan  │
└───────────┬────────────┘
            │
            │ Passes: Intake + Body + Training plan
            ▼
┌────────────────────────┐
│ Nutrition Agent        │  ◄─── Receives: Intake + Body + Training
│                        │       Generates: Nutrition plan
│ Output: Nutrition Plan │
└───────────┬────────────┘
            │
            │ Passes: ALL information
            ▼
┌────────────────────────┐
│ Head Coach Agent       │  ◄─── Receives: EVERYTHING
│                        │       Generates: Integrated program
│ Output: Final Program  │
└────────────────────────┘

KEY CONCEPT: Each agent builds upon the work of previous agents
```

---

## 🎯 Key Concepts Demonstrated

### 1. Sequential Multi-Agent System
- **5 specialized agents** working in sequence
- Each agent receives context from previous agents
- Information flows forward through the chain

### 2. Tool Integration
- **Built-in**: Google Search (all agents)
- **Custom**: A2A communication tools (head coach only)
- **Memory**: PreloadMemoryTool (all agents)

### 3. Session Management
- Shared `InMemorySessionService` instance
- Each agent has its own session (scoped by app_name)
- Consistent user_id and session_id across agents

### 4. Agent-to-Agent Protocol
- Head coach can call other agents via custom tools
- Tools defined in `shared/agent_communication.py`
- Enables coordination and information gathering

---

## 🔑 Key Files

| File | Purpose |
|------|---------|
| `demo.py` | Main orchestrator - runs all agents sequentially |
| `reception_agent/agent.py` | Client information collection |
| `body_scanner_agent/agent.py` | Body analysis and movement assessment |
| `pt_agent/agent.py` | Training plan creation |
| `nutrition_agent/agent.py` | Nutrition plan design |
| `head_coach_agent/agent.py` | Coordinator with A2A tools |
| `shared/agent_communication.py` | A2A protocol implementation |

---

**This architecture demonstrates a production-ready multi-agent system with proper separation of concerns, sequential information flow, and agent coordination.**

