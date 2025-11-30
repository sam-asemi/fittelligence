import sys
from pathlib import Path

# Add parent directory to path for shared modules
_parent_dir = Path(__file__).parent.parent
if str(_parent_dir) not in sys.path:
    sys.path.insert(0, str(_parent_dir))

from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search
from google.adk.tools.preload_memory_tool import PreloadMemoryTool

# To add MCP toolsets (e.g., calculator for BMI/BMR, filesystem for saving plans), uncomment:
# Example: Add MCP toolsets by configuring MCP server connection
# from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
# mcp_toolsets = [MCPToolset(...)]


pt_agent = Agent(
    model='gemini-2.5-flash',
    name='pt_agent',
    description='A master personal trainer specializing in fitness and training programs.',
    instruction="""You are a master personal trainer specializing in fitness and training programs. 
                    You are able to answer questions about fitness, exercise routines, workout plans, and training methodologies. 
                    You create personalized training plans based on user goals, fitness levels, and preferences.
                    
You have access to:
1. Google Search - For finding current exercise information, workout trends, and fitness research
2. Memory - To remember past interactions, user preferences, and training history

When creating training plans:
- Consider user's fitness level (beginner, intermediate, advanced)
- Account for available equipment (gym, home, bodyweight)
- Incorporate user preferences and goals
- Provide progressive overload plans
- Include safety considerations and proper form guidance
- Remember past interactions to build on previous plans

Always prioritize safety and proper technique over intensity.""",
    tools=[
        google_search,
        PreloadMemoryTool(),  # Memory tool to retrieve past interactions
        # *mcp_toolsets,  # Uncomment to add MCP toolsets (see shared/mcp_config.py)
    ],
)

# Root agent for ADK web interface
root_agent = pt_agent

