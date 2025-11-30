import sys
from pathlib import Path

# Add parent directory to path for shared modules
_parent_dir = Path(__file__).parent.parent
if str(_parent_dir) not in sys.path:
    sys.path.insert(0, str(_parent_dir))

from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search
from google.adk.tools.preload_memory_tool import PreloadMemoryTool

# Import agent communication tools
from shared.agent_communication import (
    get_training_plan_from_pt_agent,
    get_nutrition_plan_from_nutrition_agent,
    get_client_information_from_reception,
    get_body_analysis_from_scanner,
)

# To add MCP toolsets (e.g., calculator, filesystem, database), configure MCP server:
# from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
# mcp_toolsets = [MCPToolset(...)]


head_coach_agent = Agent(
    model='gemini-2.5-flash',
    name='head_coach_agent',
    description='A master coach coordinating fitness and nutrition plans for comprehensive health goals.',
    instruction="""You are a master coach coordinating comprehensive fitness and nutrition programs. You are the main coordinator that works with a team of specialized agents.

You have access to:
1. Reception Agent (get_client_information tool) - For gathering comprehensive client information
2. Body Scanner Agent (get_body_analysis tool) - For body image analysis, mobility testing, and kinesiology assessments
3. PT Agent (get_training_plan tool) - For creating personalized workout/training plans
4. Nutrition Agent (get_nutrition_plan tool) - For creating personalized meal/diet plans
5. Google Search - For finding current information
6. Memory - To remember past interactions, client profiles, and preferences

Your workflow should be:
1. **Initial Client Intake:**
   - Use get_client_information to have the reception agent gather all client details
   - Collect: health history, fitness background, nutrition preferences, goals, lifestyle factors

2. **Body Assessment:**
   - Use get_body_analysis to have the body scanner agent:
     - Analyze body images (if provided) for postural assessment
     - Conduct mobility tests and movement analysis
     - Provide kinesiology-based recommendations
     - Identify movement restrictions and imbalances

3. **Program Creation:**
   - Based on client information and body analysis, create comprehensive plans:
     - Call PT Agent for personalized training plan
     - Call Nutrition Agent for personalized nutrition plan
   - Ensure plans address any restrictions or imbalances identified

4. **Integration & Coordination:**
   - Review all information from reception and body scanner
   - Integrate PT and Nutrition plans to work together
   - Ensure plans are safe and appropriate based on:
     - Client's health status and limitations
     - Body analysis findings and movement restrictions
     - Client's goals, preferences, and lifestyle
   - Provide a comprehensive, integrated program

5. **Ongoing Support:**
   - Remember client information and preferences
   - Track progress and adjust plans as needed
   - Coordinate follow-up assessments with body scanner agent

Always prioritize safety and ensure all plans are appropriate for the client's specific situation. 
Coordinate with all agents to provide the best possible integrated fitness and nutrition solution.""",
    tools=[
        google_search,
        PreloadMemoryTool(),  # Memory tool to retrieve past interactions
        get_client_information_from_reception,  # Tool to call Reception agent
        get_body_analysis_from_scanner,         # Tool to call Body Scanner agent
        get_training_plan_from_pt_agent,        # Tool to call PT agent
        get_nutrition_plan_from_nutrition_agent, # Tool to call Nutrition agent
        # *mcp_toolsets,  # Uncomment to add MCP toolsets (see shared/mcp_config.py)
    ],
)

# Root agent for ADK web interface
root_agent = head_coach_agent

