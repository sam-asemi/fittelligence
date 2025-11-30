# FitTelligence - Kaggle Project Submission

## Project Overview

**Track:** Concierge Agents

### Problem Statement

Creating personalized fitness and nutrition programs is currently a **time-intensive, fragmented, and expensive process** that requires:
- Multiple specialist consultations (reception/intake, body assessment, personal trainer, nutritionist)
- Manual coordination across different professionals
- High cost barriers ($400-2000+ per complete program)
- Time constraints (6-12 hours total process time)

**Current Process:**
- Reception/intake: 1-2 hours
- Body assessment: 1-2 hours
- Training plan: 2-4 hours
- Nutrition plan: 1-2 hours
- Program coordination: 1-2 hours
- **Total: 6-12 hours + $400-2000 in costs**

### Solution Pitch

**FitTelligence** is an automated multi-agent AI system that coordinates **5 specialized agents** working in sequence to automatically generate comprehensive, personalized fitness and nutrition programs:

1. **Reception Agent** - Collects comprehensive client information
2. **Body Scanner Agent** - Analyzes movement and provides kinesiology-based assessment
3. **PT Agent** - Creates personalized training plans
4. **Nutrition Agent** - Designs customized nutrition programs
5. **Head Coach Agent** - Integrates everything into a cohesive program

**Key Innovation:** All agents work together seamlessly with context flowing sequentially between them, eliminating manual coordination.

**Process Transformation:**
- **Before:** 6-12 hours, $400-2000, multiple appointments
- **After:** Minutes, accessible 24/7, comprehensive program

### Value Proposition

- ⏱️ **Time Savings:** Reduces program creation from 6-12 hours to minutes
- 💰 **Cost Reduction:** Eliminates $400-2000 in consultation costs
- 🎯 **Quality:** Comprehensive, integrated programs with specialized expertise
- 📈 **Scalability:** 24/7 availability, no scheduling constraints
- 🧠 **Personalization:** Multi-agent expertise with memory integration
- ✅ **Consistency:** Standardized quality across all clients

## ✅ Demonstrated Concepts

### 1. Multi-Agent System (Sequential Agents) ✓

**Implementation:** 5 specialized agents working in sequence:
- `reception_agent/` - Client information collection
- `body_scanner_agent/` - Body analysis and kinesiology assessment
- `pt_agent/` - Training plan creation
- `nutrition_agent/` - Nutrition plan design
- `head_coach_agent/` - Coordinator integrating all agents

**Sequential Flow:**
Each agent receives context from previous agents and passes information to the next.

**Files:**
- `reception_agent/agent.py`
- `body_scanner_agent/agent.py`
- `pt_agent/agent.py`
- `nutrition_agent/agent.py`
- `head_coach_agent/agent.py`

**Demo:** Run `python demo.py` to see sequential agent flow

### 2. Tools ✓

#### Built-in Tools
- **Google Search** - Integrated in all agents via `google.adk.tools.google_search`

#### Custom Tools
- **Agent-to-Agent Communication Tools** - Custom functions allowing agents to call each other
  - Located in `shared/agent_communication.py`
  - Functions: `get_client_information_from_reception()`, `get_body_analysis_from_scanner()`, etc.
  - Used by `head_coach_agent` to coordinate other agents

#### MCP-Ready Architecture
- MCP integration examples are commented in agent files
- Ready for OpenAPI tools and external MCP integrations

**Files:**
- `shared/agent_communication.py` - Custom A2A tools
- All agent files demonstrate tool usage (with MCP examples commented)

### 3. Sessions & Memory ✓

#### Sessions & State Management
- **InMemorySessionService** - Used for session management
- Consistent session IDs across sequential agents
- State persistence throughout agent workflow

#### Long-term Memory
- **PreloadMemoryTool** - Integrated in all agents
- Enables agents to remember past interactions
- Maintains context across conversations

#### Memory Configuration
- Agents use `PreloadMemoryTool()` directly for long-term memory
- Session management via `InMemorySessionService` (demonstrated in demo.py)
- Ready for VertexAiMemoryBankService in production

**Files:**
- All agent files include `PreloadMemoryTool()`
- `demo.py` demonstrates session management with `InMemorySessionService`

### 4. Agent-to-Agent (A2A) Protocol ✓

**Implementation:**
- Custom tools in `shared/agent_communication.py` enable agent-to-agent calls
- `head_coach_agent` uses these tools to coordinate other agents
- Sequential information passing through agent communication

**Files:**
- `shared/agent_communication.py` - A2A protocol implementation
- `head_coach_agent/agent.py` - Uses A2A tools

## 📁 Project Structure

```
fittelligence-1/
├── demo.py                          # Main demonstration script
├── README.md                        # Full documentation
├── KAGGLE_SUBMISSION.md            # This file
├── requirements.txt                 # Dependencies
│
├── reception_agent/                 # Agent 1: Client intake
│   ├── __init__.py
│   └── agent.py
│
├── body_scanner_agent/              # Agent 2: Body analysis
│   ├── __init__.py
│   └── agent.py
│
├── pt_agent/                        # Agent 3: Training plans
│   ├── __init__.py
│   └── agent.py
│
├── nutrition_agent/                 # Agent 4: Nutrition plans
│   ├── __init__.py
│   └── agent.py
│
├── head_coach_agent/                # Agent 5: Coordinator
│   ├── __init__.py
│   └── agent.py
│
└── shared/                          # Shared utilities
    ├── __init__.py
    └── agent_communication.py      # A2A tools
```

## 🚀 Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set API key:**
   ```bash
   export GOOGLE_API_KEY="your-api-key"
   ```

3. **Run demo:**
   ```bash
   python demo.py
   ```

## 📊 Key Features

### Multi-Agent Sequential Flow
- Reception → Body Scanner → PT → Nutrition → Head Coach
- Each agent receives context from previous agents
- Information flows sequentially through the system

### Tool Integration
- Built-in: Google Search in all agents
- Custom: A2A communication tools
- MCP-ready: Architecture supports additional tools

### Memory & Sessions
- Session management with InMemorySessionService
- Long-term memory with PreloadMemoryTool
- Context retention across agent interactions

### A2A Protocol
- Head coach can call other agents via custom tools
- Sequential data passing mechanism
- Coordinated multi-agent workflow

## 🎯 Submission Checklist

- [x] Multi-agent system (5 sequential agents)
- [x] Built-in tools (Google Search)
- [x] Custom tools (A2A communication)
- [x] MCP-ready architecture
- [x] Sessions & state management (InMemorySessionService)
- [x] Long-term memory (PreloadMemoryTool)
- [x] Agent-to-agent protocol (custom tools)
- [x] Working demo script
- [x] Complete documentation

## 📝 Notes for Evaluators

1. **Run the demo:** `python demo.py` shows all concepts in action
2. **Check agents:** Each agent folder contains specialized agent implementation
3. **A2A Protocol:** See `shared/agent_communication.py` and `head_coach_agent/agent.py`
4. **Memory:** All agents include `PreloadMemoryTool()` and use session management
5. **Tools:** Google Search is in all agents; custom tools in shared folder

## 🔍 Key Files to Review

1. **`demo.py`** - Complete demonstration of all concepts
2. **`head_coach_agent/agent.py`** - Shows A2A tool usage
3. **`shared/agent_communication.py`** - Custom tool implementation
4. **Any agent file** - Shows tool integration and memory usage (PreloadMemoryTool)

---

**This submission demonstrates mastery of multi-agent systems, tools, sessions & memory, and A2A protocol using Google ADK.**

