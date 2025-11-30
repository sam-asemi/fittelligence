# Using ADK Web UI

You can also use the Google ADK Web UI to interact with your agents through a browser interface.

## Setup

1. **Make sure your agent is exported as `root_agent`:**
   
   Each agent file should have:
   ```python
   root_agent = reception_agent  # or whichever agent you want to use
   ```

2. **Run ADK Web UI:**
   ```bash
   adk web
   ```
   
   Or if you have a specific agent directory:
   ```bash
   cd reception_agent
   adk web
   ```

3. **Access the UI:**
   - Open your browser to the URL shown (typically `http://localhost:8080`)
   - You'll see a chat interface where you can interact with the agent

## Using Multiple Agents

Since each agent is in its own directory, you can:

1. **Run different agents in different terminals:**
   ```bash
   # Terminal 1 - Reception Agent
   cd reception_agent
   adk web --port 8080
   
   # Terminal 2 - Body Scanner Agent
   cd body_scanner_agent
   adk web --port 8081
   
   # Terminal 3 - PT Agent
   cd pt_agent
   adk web --port 8082
   ```

2. **Or use the head coach agent** which can coordinate all others:
   ```bash
   cd head_coach_agent
   adk web
   ```

## Features

- **Chat Interface**: Natural language conversation with agents
- **Session Management**: Conversations are saved in sessions
- **Memory**: Agents remember past interactions
- **Tool Usage**: See when agents use tools (Google Search, etc.)

## Limitations

- ADK Web UI shows one agent at a time
- For sequential multi-agent flow, use the `demo.py` script
- The terminal-based demo shows the full sequential workflow

## Recommendation

For the capstone project demonstration:
- Use `demo.py` to show the complete sequential multi-agent workflow
- Use ADK Web UI for individual agent testing or demonstrations

