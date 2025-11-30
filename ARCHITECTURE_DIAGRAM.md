# FitTelligence - Architecture Diagram

## Visual Architecture (Mermaid Diagram)

GitHub will automatically render this Mermaid diagram:

```mermaid
graph TB
    User[👤 User Input<br/>Terminal / ADK UI] --> Demo[demo.py<br/>Orchestrator]
    
    Demo --> Session[InMemorySessionService<br/>Session Management]
    Demo --> Memory[PreloadMemoryTool<br/>Long-term Memory]
    Demo --> Tools[Google Search<br/>Built-in Tool]
    
    Demo --> Agent1[1️⃣ Reception Agent<br/>Client Intake]
    Agent1 -->|Client Profile| Agent2[2️⃣ Body Scanner Agent<br/>Body Analysis]
    Agent2 -->|+ Body Analysis| Agent3[3️⃣ PT Agent<br/>Training Plan]
    Agent3 -->|+ Training Plan| Agent4[4️⃣ Nutrition Agent<br/>Nutrition Plan]
    Agent4 -->|+ Nutrition Plan| Agent5[5️⃣ Head Coach Agent<br/>Coordinator]
    
    Agent5 -->|Uses A2A Tools| A2A[shared/agent_communication.py<br/>A2A Protocol]
    A2A -->|Can Call| Agent1
    A2A -->|Can Call| Agent2
    A2A -->|Can Call| Agent3
    A2A -->|Can Call| Agent4
    
    Agent5 --> Final[✅ Final Integrated Program<br/>Training + Nutrition]
    
    style User fill:#e1f5ff
    style Demo fill:#fff4e1
    style Agent1 fill:#e8f5e9
    style Agent2 fill:#e8f5e9
    style Agent3 fill:#e8f5e9
    style Agent4 fill:#e8f5e9
    style Agent5 fill:#fff3e0
    style Final fill:#f3e5f5
    style A2A fill:#e3f2fd
```

## Sequential Flow Diagram

```mermaid
sequenceDiagram
    participant User
    participant Demo as demo.py
    participant R as Reception Agent
    participant B as Body Scanner Agent
    participant P as PT Agent
    participant N as Nutrition Agent
    participant H as Head Coach Agent
    
    User->>Demo: Provide client information
    Demo->>R: Process client intake
    R-->>Demo: Client Profile
    
    Demo->>B: Analyze body (with client context)
    B-->>Demo: Body Analysis
    
    Demo->>P: Create training plan (with intake + body)
    P-->>Demo: Training Plan
    
    Demo->>N: Create nutrition plan (with all context)
    N-->>Demo: Nutrition Plan
    
    Demo->>H: Integrate everything
    H->>H: Use A2A tools to coordinate
    H-->>Demo: Final Integrated Program
    
    Demo-->>User: Complete Program
```

## Agent Relationship Diagram

```mermaid
graph LR
    subgraph "Sequential Flow"
        A1[Reception Agent] -->|Client Profile| A2[Body Scanner Agent]
        A2 -->|+ Body Analysis| A3[PT Agent]
        A3 -->|+ Training Plan| A4[Nutrition Agent]
        A4 -->|+ Nutrition Plan| A5[Head Coach Agent]
    end
    
    subgraph "A2A Communication"
        A5 -->|get_client_information| A1
        A5 -->|get_body_analysis| A2
        A5 -->|get_training_plan| A3
        A5 -->|get_nutrition_plan| A4
    end
    
    A5 --> Final[Final Program]
    
    style A1 fill:#c8e6c9
    style A2 fill:#c8e6c9
    style A3 fill:#c8e6c9
    style A4 fill:#c8e6c9
    style A5 fill:#ffcc80
    style Final fill:#ce93d8
```

## System Architecture

```mermaid
graph TB
    subgraph "Input Layer"
        UI1[Terminal Input]
        UI2[ADK Web UI]
    end
    
    subgraph "Orchestration Layer"
        Demo[demo.py<br/>Orchestrator]
    end
    
    subgraph "Service Layer"
        Session[InMemorySessionService]
        Memory[PreloadMemoryTool]
        Search[Google Search]
    end
    
    subgraph "Agent Layer - Sequential"
        A1[Reception Agent]
        A2[Body Scanner Agent]
        A3[PT Agent]
        A4[Nutrition Agent]
        A5[Head Coach Agent]
    end
    
    subgraph "A2A Protocol"
        A2ATools[agent_communication.py]
    end
    
    subgraph "Output"
        Program[Final Integrated Program]
    end
    
    UI1 --> Demo
    UI2 --> Demo
    Demo --> Session
    Demo --> Memory
    Demo --> Search
    
    Demo --> A1
    A1 --> A2
    A2 --> A3
    A3 --> A4
    A4 --> A5
    
    A5 --> A2ATools
    A2ATools -.->|Can Call| A1
    A2ATools -.->|Can Call| A2
    A2ATools -.->|Can Call| A3
    A2ATools -.->|Can Call| A4
    
    A5 --> Program
    
    style Demo fill:#fff4e1
    style A1 fill:#e8f5e9
    style A2 fill:#e8f5e9
    style A3 fill:#e8f5e9
    style A4 fill:#e8f5e9
    style A5 fill:#fff3e0
    style Program fill:#f3e5f5
```

---

## 📸 How to Generate an Image

### Option 1: Use Mermaid Live Editor
1. Go to https://mermaid.live/
2. Copy any of the Mermaid diagrams above
3. Click "Export" → "PNG" or "SVG"
4. Save the image

### Option 2: Use GitHub
- GitHub automatically renders Mermaid diagrams in markdown files
- Just view `ARCHITECTURE_DIAGRAM.md` on GitHub

### Option 3: Use Online Tools
- **Mermaid.ink**: https://mermaid.ink/ (generates images from Mermaid code)
- **Kroki**: https://kroki.io/ (supports Mermaid)

### Option 4: Use Python (diagrams library)
```python
# Install: pip install diagrams
from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import User
from diagrams.programming.language import Python
from diagrams.onprem.compute import Server

with Diagram("FitTelligence Architecture", show=False):
    user = User("User")
    demo = Python("demo.py")
    
    with Cluster("Agents"):
        agents = [
            Python("Reception"),
            Python("Body Scanner"),
            Python("PT"),
            Python("Nutrition"),
            Python("Head Coach")
        ]
    
    user >> demo >> agents[0] >> agents[1] >> agents[2] >> agents[3] >> agents[4]
```

---

## 🎨 Visual Summary

The architecture shows:
- **5 Sequential Agents** working in a pipeline
- **Shared Services** (Session, Memory, Tools)
- **A2A Protocol** for agent coordination
- **Information Flow** from user input to final program

