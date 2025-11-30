# FitTelligence - Multi-Agent Fitness Coaching System

A comprehensive multi-agent system demonstrating advanced ADK concepts for fitness and nutrition coaching.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

## 🎯 Quick Links

- **[Kaggle Submission Writeup](SUBMISSION_WRITEUP.md)** - Complete project submission document
- **[Kaggle Technical Details](KAGGLE_SUBMISSION.md)** - Technical implementation details

## 🎯 Project Overview

**Problem:** Creating personalized fitness and nutrition programs is time-intensive (6-12 hours), expensive ($400-2000), and requires coordinating multiple specialists.

**Solution:** FitTelligence uses **5 specialized AI agents** working together in a sequential pattern to automatically generate comprehensive, personalized fitness and nutrition programs in minutes instead of days.

**Track:** Concierge Agents

**Value:** Reduces program creation time from 6-12 hours to minutes, eliminates $400-2000 in consultation costs, and provides 24/7 access to comprehensive coaching services.

## 📊 System Architecture

![FitTelligence Architecture](architecture_diagram.png)

*Complete system architecture showing the sequential flow of 5 specialized agents, shared services, and agent-to-agent communication protocol.*

## ✨ Key Concepts Demonstrated

### 1. Multi-Agent System (Sequential Agents) ✓

The system features **5 specialized agents** working in sequence:

- **Reception Agent** - Collects comprehensive client information
- **Body Scanner Agent** - Analyzes body posture and movement patterns using kinesiology expertise
- **PT Agent** - Creates personalized training plans based on client goals
- **Nutrition Agent** - Designs customized nutrition plans
- **Head Coach Agent** - Coordinates all agents and integrates everything into a complete program

**Sequential Flow:**
```
Reception → Body Scanner → PT Agent → Nutrition Agent → Head Coach
Each agent receives context from previous agents in the sequence
```

### 2. Tools ✓

#### Built-in Tools
- **Google Search** - Available to all agents for current information

#### Custom Tools
- **Agent-to-Agent Communication Tools** (`shared/agent_communication.py`)
  - `get_client_information_from_reception()` - Head coach can request client info
  - `get_body_analysis_from_scanner()` - Head coach can request body analysis
  - `get_training_plan_from_pt_agent()` - Head coach can request training plans
  - `get_nutrition_plan_from_nutrition_agent()` - Head coach can request nutrition plans

#### MCP-Ready Architecture
- MCP integration examples are commented in agent files
- Architecture supports adding MCP servers for additional tool capabilities

### 3. Sessions & Memory ✓

#### Session Management
- **InMemorySessionService** - Session state management for each agent
- Consistent session across sequential agent interactions
- Session persistence for context continuity

#### Long-term Memory
- **PreloadMemoryTool** - Enables agents to remember past interactions
- Memory integration in all agents for personalized responses
- Context retention across conversations

#### Memory Configuration
- Agents use `PreloadMemoryTool()` directly for long-term memory
- Session management via `InMemorySessionService` (as shown in demo.py)
- Ready for VertexAiMemoryBankService in production

### 4. Agent-to-Agent (A2A) Protocol ✓

- **Custom Tools Implementation** - Head coach agent has tools to call other agents
- **Sequential Data Passing** - Context flows between agents through conversation and agent communication tools
- **Information Integration** - Each agent receives relevant context from previous agents
- **Coordinated Workflow** - Head coach orchestrates the entire process

## 📁 Project Structure

```
fittelligence-1/
├── demo.py                          # Main demo script
├── README.md                        # This file
├── requirements.txt                 # Python dependencies
│
├── reception_agent/                 # Client intake agent
│   ├── __init__.py
│   └── agent.py
│
├── body_scanner_agent/              # Body analysis agent
│   ├── __init__.py
│   └── agent.py
│
├── pt_agent/                        # Training plan agent
│   ├── __init__.py
│   └── agent.py
│
├── nutrition_agent/                 # Nutrition plan agent
│   ├── __init__.py
│   └── agent.py
│
├── head_coach_agent/                # Coordinator agent
│   ├── __init__.py
│   └── agent.py                    # Uses A2A tools to call other agents
│
└── shared/                          # Shared utilities
    ├── __init__.py
    └── agent_communication.py      # A2A Protocol implementation
```

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Google ADK installed
- Google API key

### Installation

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up API credentials:**
   
   **Option A: Google AI API Key (Recommended)**
   ```bash
   export GOOGLE_API_KEY="your-api-key-here"
   ```
   
   Or create a `.env` file:
   ```bash
   echo "GOOGLE_API_KEY=your-api-key-here" > .env
   ```
   
   **Option B: Vertex AI**
   ```bash
   export GOOGLE_CLOUD_PROJECT="your-project-id"
   export GOOGLE_CLOUD_LOCATION="us-central1"
   gcloud auth application-default login
   ```

### Running the Demo

**Option 1: Interactive Terminal Input (Recommended)**

```bash
python demo.py
```

The demo will:
1. Prompt you to enter client information interactively (or use demo data)
2. Collect: name, age, weight, height, gender, activity level, fitness goals, experience, equipment, medical conditions
3. Run all 5 agents sequentially with your personalized information
4. Show complete workflow from intake to final integrated program

**Option 2: ADK Web UI**

For individual agent interaction through a browser:

```bash
# Run a specific agent
cd reception_agent
adk web

# Or run head coach agent (can coordinate others)
cd head_coach_agent
adk web
```

See [ADK_UI_GUIDE.md](ADK_UI_GUIDE.md) for more details.

**What You'll See:**

The demo runs through the complete sequential agent workflow:
- Reception agent collecting client information
- Body scanner agent analyzing the client
- PT agent creating a training plan
- Nutrition agent creating a nutrition plan
- Head coach agent integrating everything

## 🔧 Architecture Details

### Sequential Agent Flow

1. **Reception Agent** collects client information
   - Uses: Google Search, PreloadMemoryTool

2. **Body Scanner Agent** analyzes body and movement
   - Uses: Google Search (for kinesiology research), PreloadMemoryTool
   - Receives: Client information from reception agent

3. **PT Agent** creates training plan
   - Uses: Google Search, PreloadMemoryTool
   - Receives: Client info + body analysis

4. **Nutrition Agent** creates nutrition plan
   - Uses: Google Search, PreloadMemoryTool
   - Receives: Client info + body analysis + training plan

5. **Head Coach Agent** integrates everything
   - Uses: Google Search, PreloadMemoryTool, A2A communication tools
   - Receives: All information from previous agents
   - Can call other agents via custom tools

### Session Management

All agents use `InMemorySessionService` with consistent session IDs to maintain context across the sequential workflow.

### Memory Integration

Each agent includes `PreloadMemoryTool()` to:
- Remember past client interactions
- Recall preferences and goals
- Build on previous conversations
- Maintain personalized context

### A2A Communication

The head coach agent includes custom tools (defined in `shared/agent_communication.py`) that allow it to:
- Request client information from reception agent
- Request body analysis from body scanner agent
- Request training plans from PT agent
- Request nutrition plans from nutrition agent

These tools demonstrate the Agent-to-Agent protocol pattern.

## 📚 Key Features

### Reception Agent
- Comprehensive client intake
- Health history collection
- Fitness background assessment
- Goal identification

### Body Scanner Agent
- Body posture analysis
- Mobility testing protocols
- Movement pattern assessment
- Kinesiology-based recommendations
- Injury risk evaluation

### PT Agent
- Personalized workout programs
- Exercise selection and progression
- Sets, reps, and rest period planning
- Safety considerations

### Nutrition Agent
- Personalized meal plans
- Macronutrient calculation
- Dietary restriction handling
- Meal timing recommendations

### Head Coach Agent
- Coordinates all other agents
- Integrates training and nutrition plans
- Ensures program coherence
- Provides comprehensive final program

## 🛠️ Configuration

### Memory Service

Default: In-memory storage for development

For production with persistent memory, configure Vertex AI Memory Bank. Agents currently use `PreloadMemoryTool()` directly for memory functionality.

### MCP Servers

Add Model Context Protocol servers by uncommenting and configuring the MCP examples in agent files. The architecture is ready to integrate additional MCP tools.

## 📊 Example Usage

```python
from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from reception_agent import reception_agent

# Create session
session_service = InMemorySessionService()
session_service.create_session_sync(
    user_id="user1",
    session_id="session1",
    app_name="reception_agent"
)

# Run agent
runner = Runner(
    agent=reception_agent,
    session_service=session_service,
    user_id="user1",
    session_id="session1"
)

# Get response
for event in runner.run("I want to start a fitness program"):
    if hasattr(event, 'content') and hasattr(event.content, 'parts'):
        for part in event.content.parts:
            if hasattr(part, 'text'):
                print(part.text)
```

## 🎓 Learning Outcomes

This project demonstrates:

1. **Multi-Agent Architecture** - Building systems with multiple specialized agents
2. **Sequential Agent Flow** - Passing context between agents in sequence
3. **Tool Integration** - Using built-in and custom tools
4. **Session Management** - Maintaining state across agent interactions
5. **Memory Systems** - Long-term memory for personalized experiences
6. **A2A Protocol** - Agent-to-agent communication patterns
7. **System Design** - Coordinating complex multi-agent workflows

## 📝 Notes

- All agents are configured with `gemini-2.5-flash` model
- Session management ensures context continuity
- Memory tools enable personalized, context-aware responses
- A2A tools allow the head coach to coordinate other agents
- MCP architecture is ready for additional tool integrations

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Built with ❤️ using Google ADK to demonstrate advanced multi-agent system concepts**

## 🤝 Contributing

This is a capstone project submission. Contributions and feedback are welcome!

## 📞 Support

For questions about this project, please open an issue on GitHub or refer to the documentation files.

## 🙏 Acknowledgments

- Google ADK for the agent development framework
- All the course instructors and resources that made this project possible
