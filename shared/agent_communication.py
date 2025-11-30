"""
Agent-to-agent communication tools for head_coach_agent
"""
import sys
from pathlib import Path

# Add parent directory to path for cross-agent imports
_parent_dir = Path(__file__).parent.parent
if str(_parent_dir) not in sys.path:
    sys.path.insert(0, str(_parent_dir))


def get_training_plan_from_pt_agent(user_goals: str, fitness_level: str = "intermediate", preferences: str = "") -> str:
    """
    Get a personalized training plan from the PT agent.
    
    Args:
        user_goals: The user's fitness goals (e.g., "build muscle", "lose weight", "improve endurance")
        fitness_level: Current fitness level (beginner, intermediate, advanced)
        preferences: User preferences for workouts (e.g., "prefer strength training", "love running")
    
    Returns:
        A detailed training plan from the PT agent
    """
    try:
        # Import pt_agent dynamically
        from pt_agent import pt_agent
        
        # Create a prompt for the pt_agent
        prompt = f"""Create a personalized training plan with the following details:
- User Goals: {user_goals}
- Fitness Level: {fitness_level}
- Preferences: {preferences}

Please provide a comprehensive training plan including:
1. Weekly workout schedule
2. Specific exercises with sets, reps, and rest periods
3. Progression plan
4. Equipment needed
5. Safety considerations

Format the response clearly and be specific."""
        
        # Note: In actual implementation, you would use ADK's Runner to invoke the agent
        # For now, return a message indicating what would happen
        return f"""PT Agent Training Plan Request:
Goals: {user_goals}
Fitness Level: {fitness_level}
Preferences: {preferences}

[The PT agent would create a comprehensive training plan based on these inputs. 
To use this in production, implement agent invocation using ADK's Runner or MCP connection.]"""
        
    except ImportError:
        return "PT Agent is not available. Please ensure pt_agent is properly configured."
    except Exception as e:
        return f"Error calling PT agent: {str(e)}"


def get_nutrition_plan_from_nutrition_agent(user_goals: str, dietary_restrictions: str = "", nutritional_needs: str = "") -> str:
    """
    Get a personalized nutrition plan from the nutrition agent.
    
    Args:
        user_goals: The user's nutrition/health goals (e.g., "weight loss", "muscle gain", "maintain weight")
        dietary_restrictions: Any dietary restrictions or allergies (e.g., "vegetarian", "gluten-free", "lactose intolerant")
        nutritional_needs: Specific nutritional requirements (e.g., "high protein", "low carb", "2000 calories")
    
    Returns:
        A detailed nutrition plan from the nutrition agent
    """
    try:
        # Import nutrition_agent dynamically
        from nutrition_agent import nutrition_agent
        
        # Create a prompt for the nutrition_agent
        prompt = f"""Create a personalized nutrition plan with the following details:
- User Goals: {user_goals}
- Dietary Restrictions: {dietary_restrictions}
- Nutritional Needs: {nutritional_needs}

Please provide a comprehensive nutrition plan including:
1. Daily meal plan with specific food suggestions
2. Macronutrient breakdown (protein, carbs, fats)
3. Calorie targets
4. Meal timing recommendations
5. Recipe suggestions
6. Supplement recommendations if applicable

Format the response clearly and be specific."""
        
        # Note: In actual implementation, you would use ADK's Runner to invoke the agent
        return f"""Nutrition Agent Plan Request:
Goals: {user_goals}
Dietary Restrictions: {dietary_restrictions}
Nutritional Needs: {nutritional_needs}

[The Nutrition agent would create a comprehensive nutrition plan based on these inputs.
To use this in production, implement agent invocation using ADK's Runner or MCP connection.]"""
        
    except ImportError:
        return "Nutrition Agent is not available. Please ensure nutrition_agent is properly configured."
    except Exception as e:
        return f"Error calling Nutrition agent: {str(e)}"


def get_client_information_from_reception(
    client_name: str = "",
    additional_questions: str = ""
) -> str:
    """
    Get comprehensive client information from the reception agent.
    
    Args:
        client_name: Name of the client (optional)
        additional_questions: Any specific information needed beyond standard intake
    
    Returns:
        Comprehensive client information profile
    """
    try:
        # Import reception_agent dynamically
        from reception_agent import reception_agent
        
        # Create a prompt for the reception_agent
        prompt = f"""Collect comprehensive client information.
        
Client Name: {client_name if client_name else "[New Client]"}
Additional Information Needed: {additional_questions if additional_questions else "Standard intake"}

Please gather all necessary information including:
1. Personal information and demographics
2. Health and medical history
3. Fitness background and experience
4. Nutrition preferences and restrictions
5. Lifestyle factors
6. Goals and expectations

Provide a detailed client profile summary."""
        
        # Note: In actual implementation, you would use ADK's Runner to invoke the agent
        return f"""Reception Agent - Client Information Collection:
Client: {client_name if client_name else "New Client"}
Request: {additional_questions if additional_questions else "Complete client intake"}

[The reception agent would conduct a thorough client intake interview and provide a comprehensive client profile.
To use this in production, implement agent invocation using ADK's Runner or MCP connection.]"""
        
    except ImportError:
        return "Reception Agent is not available. Please ensure reception_agent is properly configured."
    except Exception as e:
        return f"Error calling Reception agent: {str(e)}"


def get_body_analysis_from_scanner(
    body_images: str = "",
    mobility_test_request: str = "",
    assessment_type: str = "comprehensive"
) -> str:
    """
    Get body analysis and mobility assessment from the body scanner agent.
    
    Args:
        body_images: Description or reference to body images to analyze
        mobility_test_request: Specific mobility tests to conduct
        assessment_type: Type of assessment (comprehensive, postural, mobility, performance)
    
    Returns:
        Detailed body analysis and recommendations
    """
    try:
        # Import body_scanner_agent dynamically
        from body_scanner_agent import body_scanner_agent
        
        # Create a prompt for the body_scanner_agent
        prompt = f"""Conduct {assessment_type} body analysis and assessment.
        
Body Images: {body_images if body_images else "No images provided yet - request images if needed"}
Mobility Test Request: {mobility_test_request if mobility_test_request else "Standard mobility assessment"}
Assessment Type: {assessment_type}

Please provide:
1. Postural analysis from images (if provided)
2. Mobility test results and recommendations
3. Movement quality assessment
4. Identified imbalances or restrictions
5. Corrective exercise recommendations
6. Performance considerations for the head coach"""
        
        # Note: In actual implementation, you would use ADK's Runner to invoke the agent
        return f"""Body Scanner Agent - Analysis Request:
Assessment Type: {assessment_type}
Images: {"Provided" if body_images else "Not provided"}
Mobility Tests: {mobility_test_request if mobility_test_request else "Standard assessment"}

[The body scanner agent would analyze body images, conduct mobility tests, and provide detailed kinesiology-based recommendations.
To use this in production, implement agent invocation using ADK's Runner or MCP connection.]"""
        
    except ImportError:
        return "Body Scanner Agent is not available. Please ensure body_scanner_agent is properly configured."
    except Exception as e:
        return f"Error calling Body Scanner agent: {str(e)}"


# These functions will be used directly as tools in the agent
# ADK agents can use callable functions directly as tools

