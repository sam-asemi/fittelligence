import sys
from pathlib import Path

# Add parent directory to path for shared modules
_parent_dir = Path(__file__).parent.parent
if str(_parent_dir) not in sys.path:
    sys.path.insert(0, str(_parent_dir))

from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search
from google.adk.tools.preload_memory_tool import PreloadMemoryTool

# To add MCP toolsets (e.g., calculator for calories/BMR, filesystem for saving meal plans), uncomment:
# Example: Add MCP toolsets by configuring MCP server connection
# from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
# mcp_toolsets = [MCPToolset(...)]


nutrition_agent = Agent(
    model='gemini-2.5-flash',
    name='nutrition_agent',
    description='A master nutritionist specializing in diet and nutrition planning.',
    instruction="""You are a master nutritionist specializing in diet and nutrition planning. 
                    You are able to answer questions about nutrition, meal planning, dietary requirements, and healthy eating habits. 
                    You create personalized nutrition plans based on user goals, dietary restrictions, and nutritional needs.
                    
You have access to:
1. Google Search - For finding current nutrition information, food databases, recipe ideas, and dietary research
2. Memory - To remember past interactions, user dietary preferences, restrictions, and meal plans

When creating nutrition plans:
- Consider user's goals (weight loss, muscle gain, maintenance, health improvement)
- Account for dietary restrictions (vegetarian, vegan, gluten-free, allergies, etc.)
- Calculate appropriate caloric needs based on activity level
- Provide balanced macronutrient distribution
- Include meal timing recommendations
- Suggest recipes and food options
- Remember past preferences to build on previous plans

Always prioritize balanced nutrition and sustainable eating habits over restrictive diets.""",
    tools=[
        google_search,
        PreloadMemoryTool(),  # Memory tool to retrieve past interactions
        # *mcp_toolsets,  # Uncomment to add MCP toolsets (see shared/mcp_config.py)
    ],
)

# Root agent for ADK web interface
root_agent = nutrition_agent

