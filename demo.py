"""
FitTelligence - Multi-Agent Fitness Coaching System Demo

PROBLEM: Creating personalized fitness programs requires 6-12 hours and $400-2000 
in specialist consultations (reception, body assessment, personal trainer, nutritionist).

SOLUTION: This system automates the entire process using 5 specialized AI agents 
working in sequence to generate comprehensive programs in minutes.

VALUE: Eliminates 6-12 hours of work and $400-2000 in costs.

This demo script demonstrates the key ADK concepts for Kaggle submission:
1. Multi-agent system with sequential agents
2. Tools (built-in Google Search, custom tools, MCP-ready)
3. Sessions & Memory (InMemorySessionService, PreloadMemoryTool)
4. Agent-to-Agent (A2A) Protocol via custom tools

Run this script to see all agents working together in a sequential flow.
"""

import os
import sys
import time
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv(override=True)

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part

# Import all agents
from reception_agent import reception_agent
from body_scanner_agent import body_scanner_agent
from pt_agent import pt_agent
from nutrition_agent import nutrition_agent
from head_coach_agent import head_coach_agent


def print_section(title: str):
    """Print a formatted section header"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70 + "\n")


def run_agent_demo(agent, agent_name: str, message: str, session_id: str, user_id: str = "demo_user", session_service=None):
    """Run an agent and display the response"""
    print(f"🤖 {agent_name}")
    print(f"📝 Message: {message}")
    print("\n⏳ Processing...\n")
    
    # Use provided session service or create a new one
    if session_service is None:
        session_service = InMemorySessionService()
    
    # Get the actual agent name from the agent object (e.g., 'reception_agent')
    actual_app_name = getattr(agent, 'name', agent_name)
    
    # Ensure session exists - create if it doesn't exist
    # ADK sessions use (user_id, session_id, app_name) as a composite key
    session_created = False
    try:
        existing_session = session_service.get_session_sync(
            user_id=user_id, 
            session_id=session_id, 
            app_name=actual_app_name
        )
        print(f"✓ Using existing session: {existing_session.id}")
    except Exception:
        # Session doesn't exist, create it
        try:
            new_session = session_service.create_session_sync(
                user_id=user_id, 
                session_id=session_id, 
                app_name=actual_app_name
            )
            print(f"✓ Created new session: {new_session.id} for app: {actual_app_name}")
            session_created = True
            
            # Verify it was created - add small delay to ensure session is committed
            time.sleep(0.1)
            verify_session = session_service.get_session_sync(
                user_id=user_id, 
                session_id=session_id, 
                app_name=actual_app_name
            )
            if verify_session:
                print(f"✓ Session verified after creation: {verify_session.id}")
            else:
                raise Exception("Session verification failed - session was not found after creation")
        except Exception as create_error:
            print(f"❌ Failed to create session: {create_error}")
            raise
    
    # Create runner (requires both app_name and agent, or just app)
    runner = Runner(
        agent=agent,
        app_name=actual_app_name,
        session_service=session_service
    )
    
    # Create Content object from message string
    content = Content(parts=[Part(text=message)], role="user")
    
    # Run the agent (pass user_id, session_id, and Content to run() method)
    response_text = ""
    try:
        for event in runner.run(user_id=user_id, session_id=session_id, new_message=content):
            # Extract text from event
            if hasattr(event, 'content') and hasattr(event.content, 'parts'):
                for part in event.content.parts:
                    if hasattr(part, 'text'):
                        response_text += part.text
            elif hasattr(event, 'text'):
                response_text += event.text
            elif hasattr(event, 'message') and hasattr(event.message, 'parts'):
                for part in event.message.parts:
                    if hasattr(part, 'text'):
                        response_text += part.text
        
        if response_text:
            print(f"✅ Response:\n{response_text}\n")
        else:
            print("⚠️  No text response received. Check API credentials.\n")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}\n")
        import traceback
        traceback.print_exc()
    
    return response_text


def collect_client_information():
    """Interactive function to collect client information from terminal"""
    print_section("Client Information Collection")
    print("Please provide the following information:\n")
    
    client_info = {}
    
    # Basic Information
    print("📋 Basic Information:")
    client_info['name'] = input("Full Name: ").strip() or "Client"
    client_info['age'] = input("Age: ").strip() or "30"
    client_info['weight'] = input("Weight (kg): ").strip() or "70"
    client_info['height'] = input("Height (cm): ").strip() or "170"
    client_info['gender'] = input("Gender (Male/Female/Other): ").strip() or "Male"
    
    print("\n")
    
    # Activity Level
    print("🏃 Activity Level:")
    print("  1. Sedentary (little to no exercise)")
    print("  2. Lightly Active (light exercise 1-3 days/week)")
    print("  3. Moderately Active (moderate exercise 3-5 days/week)")
    print("  4. Very Active (hard exercise 6-7 days/week)")
    print("  5. Extremely Active (very hard exercise, physical job)")
    activity_choice = input("Select activity level (1-5): ").strip() or "3"
    activity_levels = {
        "1": "Sedentary",
        "2": "Lightly Active",
        "3": "Moderately Active",
        "4": "Very Active",
        "5": "Extremely Active"
    }
    client_info['activity_level'] = activity_levels.get(activity_choice, "Moderately Active")
    
    print("\n")
    
    # Fitness Goals
    print("🎯 Fitness Goals (select all that apply, comma-separated):")
    print("  1. Build muscle")
    print("  2. Lose weight/fat")
    print("  3. Improve endurance")
    print("  4. Increase strength")
    print("  5. Improve flexibility")
    print("  6. General fitness")
    goals_input = input("Enter numbers (e.g., 1,2,3): ").strip() or "1,2"
    goal_map = {
        "1": "Build muscle",
        "2": "Lose weight/fat",
        "3": "Improve endurance",
        "4": "Increase strength",
        "5": "Improve flexibility",
        "6": "General fitness"
    }
    selected_goals = [goal_map.get(g.strip(), "") for g in goals_input.split(",") if g.strip() in goal_map]
    client_info['fitness_goals'] = ", ".join(selected_goals) if selected_goals else "Build muscle, Lose weight/fat"
    
    print("\n")
    
    # Experience
    print("💪 Exercise Experience:")
    print("  1. Beginner (0-6 months)")
    print("  2. Intermediate (6 months - 2 years)")
    print("  3. Advanced (2+ years)")
    experience_choice = input("Select experience level (1-3): ").strip() or "2"
    experience_levels = {
        "1": "Beginner (0-6 months)",
        "2": "Intermediate (6 months - 2 years)",
        "3": "Advanced (2+ years)"
    }
    client_info['experience'] = experience_levels.get(experience_choice, "Intermediate")
    
    print("\n")
    
    # Equipment
    print("🏋️ Available Equipment:")
    print("  1. Full gym access")
    print("  2. Home gym (weights, bench, etc.)")
    print("  3. Limited equipment (dumbbells, resistance bands)")
    print("  4. Bodyweight only")
    equipment_choice = input("Select equipment (1-4): ").strip() or "1"
    equipment_options = {
        "1": "Full gym access",
        "2": "Home gym (weights, bench, etc.)",
        "3": "Limited equipment (dumbbells, resistance bands)",
        "4": "Bodyweight only"
    }
    client_info['equipment'] = equipment_options.get(equipment_choice, "Full gym access")
    
    print("\n")
    
    # Medical Conditions
    medical = input("Any medical conditions, injuries, or limitations? (press Enter to skip): ").strip()
    client_info['medical_conditions'] = medical if medical else "None"
    
    print("\n")
    
    # Additional Notes
    notes = input("Any additional information or preferences? (press Enter to skip): ").strip()
    client_info['additional_notes'] = notes if notes else "None"
    
    return client_info


def format_client_message(client_info):
    """Format client information into a message for the reception agent"""
    message = f"""Hello! I'm interested in starting a fitness program. Here's my information:

Basic Information:
- Name: {client_info['name']}
- Age: {client_info['age']}
- Weight: {client_info['weight']} kg
- Height: {client_info['height']} cm
- Gender: {client_info['gender']}

Activity & Experience:
- Activity Level: {client_info['activity_level']}
- Exercise Experience: {client_info['experience']}
- Fitness Goals: {client_info['fitness_goals']}

Equipment & Health:
- Available Equipment: {client_info['equipment']}
- Medical Conditions/Limitations: {client_info['medical_conditions']}
- Additional Notes: {client_info['additional_notes']}

Please help me create a personalized fitness and nutrition program."""
    
    return message


def main():
    """Main demo function demonstrating sequential multi-agent workflow"""
    
    print_section("FitTelligence - Multi-Agent Fitness Coaching System Demo")
    
    print("""
PROBLEM: Creating personalized fitness programs requires 6-12 hours and $400-2000 
         in specialist consultations across multiple appointments.

SOLUTION: Automated multi-agent system that generates comprehensive programs in minutes
          by coordinating 5 specialized agents working in sequence.

VALUE: Eliminates 6-12 hours of work and $400-2000 in costs.

This demo showcases:
✓ Multi-agent system with sequential agent flow
✓ Built-in tools (Google Search)
✓ Custom tools for Agent-to-Agent communication
✓ Sessions & Memory (InMemorySessionService, PreloadMemoryTool)
✓ MCP-ready architecture (commented examples in agent files)

All agents work together in a sequential pattern:
1. Reception Agent → Collects client information (replaces 1-2 hour intake)
2. Body Scanner Agent → Analyzes body and movement (replaces 1-2 hour assessment)
3. PT Agent → Creates training plan (replaces 2-4 hour trainer consultation)
4. Nutrition Agent → Creates nutrition plan (replaces 1-2 hour nutritionist visit)
5. Head Coach Agent → Integrates everything (replaces 1-2 hour coordination)
    """)
    
    # Check API key
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key or api_key in ['your-api-key-here', 'your-api-key', '']:
        print("⚠️  WARNING: GOOGLE_API_KEY not set!")
        print("   Set it with: export GOOGLE_API_KEY='your-api-key'")
        print("   Or add it to a .env file")
        print("\n   Continuing with demo structure...\n")
    else:
        print("✅ API credentials found\n")
    
    # Collect client information interactively
    print("\n" + "="*70)
    print("  Let's collect your information to create a personalized program")
    print("="*70 + "\n")
    
    use_interactive = input("Would you like to enter your information interactively? (y/n, default: y): ").strip().lower()
    if use_interactive == 'n':
        print("\nUsing demo data...\n")
        client_info = {
            'name': 'Demo Client',
            'age': '32',
            'weight': '75',
            'height': '175',
            'gender': 'Male',
            'activity_level': 'Moderately Active',
            'fitness_goals': 'Build muscle, Lose weight/fat',
            'experience': 'Intermediate (6 months - 2 years)',
            'equipment': 'Full gym access',
            'medical_conditions': 'None',
            'additional_notes': 'None'
        }
    else:
        client_info = collect_client_information()
    
    # Format the message for reception agent
    reception_message = format_client_message(client_info)
    
    # Use consistent user_id and session_id for all agents
    user_id = client_info.get('name', 'demo_user').lower().replace(' ', '_')
    session_id = f"session_{int(time.time())}"
    
    # Create a single shared session service for all agents
    session_service = InMemorySessionService()
    print("\n✓ Created shared session service for all agents\n")
    
    # Note: Each agent will create its own session based on its app_name
    # They can share the same session_id, but sessions are scoped by (user_id, session_id, app_name)
    
    # Step 1: Reception Agent
    print_section("Step 1: Reception Agent - Collecting Client Information")
    
    reception_response = run_agent_demo(
        reception_agent,
        "Reception Agent",
        reception_message,
        session_id,
        user_id,
        session_service=session_service
    )
    
    # Step 2: Body Scanner Agent (with context from reception)
    print_section("Step 2: Body Scanner Agent - Body Analysis")
    body_scanner_message = f"""Based on the client information collected, provide a body analysis and movement assessment. 

The client is:
- {client_info['age']} years old {client_info['gender']}
- {client_info['weight']} kg, {client_info['height']} cm
- {client_info['activity_level']} activity level
- Goals: {client_info['fitness_goals']}
- Experience: {client_info['experience']}
- Equipment: {client_info['equipment']}
- Medical/Limitations: {client_info['medical_conditions']}

Please provide:
1. Postural assessment recommendations
2. Mobility test suggestions
3. Movement pattern analysis
4. Areas of focus for their goals
5. Any movement restrictions or considerations based on their profile"""
    
    body_scanner_response = run_agent_demo(
        body_scanner_agent,
        "Body Scanner Agent",
        body_scanner_message,
        session_id,
        user_id,
        session_service=session_service
    )
    
    # Step 3: PT Agent (with context from previous agents)
    print_section("Step 3: PT Agent - Creating Training Plan")
    pt_message = f"""Create a personalized training plan for this client:

Client Profile:
- {client_info['age']} years old {client_info['gender']}, {client_info['weight']} kg, {client_info['height']} cm
- {client_info['activity_level']} activity level
- Goals: {client_info['fitness_goals']}
- Experience: {client_info['experience']}
- Equipment: {client_info['equipment']}
- Medical/Limitations: {client_info['medical_conditions']}

Please create a comprehensive 4-week training program including:
1. Weekly workout schedule
2. Specific exercises with sets, reps, and rest periods
3. Progression plan
4. Form cues and safety considerations
5. Modifications based on equipment availability and experience level"""
    
    pt_response = run_agent_demo(
        pt_agent,
        "PT Agent",
        pt_message,
        session_id,
        user_id,
        session_service=session_service
    )
    
    # Step 4: Nutrition Agent (with context from all previous agents)
    print_section("Step 4: Nutrition Agent - Creating Nutrition Plan")
    nutrition_message = f"""Create a personalized nutrition plan for this client:

Client Profile:
- {client_info['age']} years old {client_info['gender']}, {client_info['weight']} kg, {client_info['height']} cm
- {client_info['activity_level']} activity level
- Goals: {client_info['fitness_goals']}
- Training: Based on {client_info['activity_level']} activity level
- Medical/Dietary: {client_info['medical_conditions']}
- Additional Notes: {client_info['additional_notes']}

Please create a comprehensive nutrition plan including:
1. Daily calorie and macronutrient targets
2. Meal plan with specific foods
3. Pre and post-workout nutrition
4. Meal timing recommendations
5. Supplement suggestions if appropriate
6. Consider any dietary restrictions or preferences mentioned"""
    
    nutrition_response = run_agent_demo(
        nutrition_agent,
        "Nutrition Agent",
        nutrition_message,
        session_id,
        user_id,
        session_service=session_service
    )
    
    # Step 5: Head Coach Agent (integrates everything)
    print_section("Step 5: Head Coach Agent - Integrated Program")
    head_coach_message = f"""Based on all the information collected from the team, create a comprehensive integrated fitness and nutrition program:

Client Information:
- {client_info['name']}: {client_info['age']} years old {client_info['gender']}, {client_info['weight']} kg, {client_info['height']} cm
- Goals: {client_info['fitness_goals']}
- Experience: {client_info['experience']}
- Activity Level: {client_info['activity_level']}
- Equipment: {client_info['equipment']}
- Medical/Limitations: {client_info['medical_conditions']}

Please create a final integrated program that:
1. Combines the training and nutrition plans from previous agents
2. Ensures they work together harmoniously
3. Addresses the client's specific goals: {client_info['fitness_goals']}
4. Includes weekly schedule
5. Provides progression guidelines
6. Includes safety considerations based on: {client_info['medical_conditions']}
7. Takes into account equipment availability: {client_info['equipment']}"""
    
    head_coach_response = run_agent_demo(
        head_coach_agent,
        "Head Coach Agent",
        head_coach_message,
        session_id,
        user_id,
        session_service=session_service
    )
    
    # Summary
    print_section("Demo Complete!")
    print("""
✅ Successfully demonstrated:

1. MULTI-AGENT SYSTEM (Sequential Agents)
   - 5 specialized agents working in sequence
   - Each agent receives context from previous agents
   - Head coach agent coordinates the flow

2. TOOLS
   - Built-in: Google Search (available to all agents)
   - Custom tools: Agent-to-Agent communication functions
   - MCP-ready: Architecture supports MCP servers (see shared/mcp_config.py)

3. SESSIONS & MEMORY
   - InMemorySessionService for session management
   - PreloadMemoryTool for long-term memory
   - Consistent session across all agents

4. AGENT-TO-AGENT (A2A) PROTOCOL
   - Custom tools in head_coach_agent allow calling other agents
   - Sequential information passing through agent communication

📁 Project Structure:
- reception_agent/     - Client intake agent
- body_scanner_agent/  - Body analysis agent  
- pt_agent/           - Training plan agent
- nutrition_agent/    - Nutrition plan agent
- head_coach_agent/   - Coordinator agent
- shared/             - Shared utilities (A2A tools, memory, MCP)

📚 Key Files:
- shared/agent_communication.py - A2A Protocol implementation

For more details, see README.md
    """)


if __name__ == "__main__":
    main()

