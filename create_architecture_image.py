"""
Script to generate architecture diagram image

Dependencies:
- diagrams library: pip install diagrams
- graphviz system package (required by diagrams):
  - macOS: brew install graphviz
  - Linux: sudo apt-get install graphviz
  - Windows: Download from https://graphviz.org/

Note: This script is optional. Architecture diagrams can also be generated
using the Mermaid diagrams in ARCHITECTURE_DIAGRAM.md (recommended).
"""

# Optional utility script - diagrams library is NOT required for the main project
# This script is only needed if you want to generate architecture images programmatically
# Alternative: Use Mermaid diagrams in ARCHITECTURE_DIAGRAM.md (recommended)
# The ImportError is handled gracefully below - this is expected if diagrams is not installed
try:
    from diagrams import Diagram, Cluster, Edge  # type: ignore[import-untyped]
    from diagrams.onprem.client import User  # type: ignore[import-untyped]
    from diagrams.programming.language import Python  # type: ignore[import-untyped]
    from diagrams.onprem.compute import Server  # type: ignore[import-untyped]
    from diagrams.onprem.database import Influxdb  # type: ignore[import-untyped]
    from diagrams.generic.blank import Blank  # type: ignore[import-untyped]
    
    with Diagram("FitTelligence Multi-Agent Architecture", filename="architecture_diagram", show=False, direction="TB"):
        
        user = User("User Input\n(Terminal/ADK UI)")
        
        with Cluster("Orchestration"):
            demo = Python("demo.py\nOrchestrator")
        
        with Cluster("Shared Services"):
            session = Server("InMemorySessionService")
            memory = Influxdb("PreloadMemoryTool")
            search = Server("Google Search")
        
        with Cluster("Sequential Agents"):
            agent1 = Python("1. Reception Agent\nClient Intake")
            agent2 = Python("2. Body Scanner Agent\nBody Analysis")
            agent3 = Python("3. PT Agent\nTraining Plan")
            agent4 = Python("4. Nutrition Agent\nNutrition Plan")
            agent5 = Python("5. Head Coach Agent\nCoordinator")
        
        with Cluster("A2A Protocol"):
            a2a = Server("agent_communication.py\nA2A Tools")
        
        final = Blank("Final Integrated Program")
        
        # Flow
        user >> demo
        demo >> session
        demo >> memory
        demo >> search
        
        demo >> agent1
        agent1 >> agent2
        agent2 >> agent3
        agent3 >> agent4
        agent4 >> agent5
        
        agent5 >> a2a
        a2a >> agent1
        a2a >> agent2
        a2a >> agent3
        a2a >> agent4
        
        agent5 >> final
    
    print("✓ Architecture diagram generated: architecture_diagram.png")
    print("  Install requirements: pip install diagrams graphviz")
    
except ImportError:
    print("""
⚠️  Diagrams library not installed.

This script is OPTIONAL. You have better alternatives:

📊 RECOMMENDED: Use Mermaid diagrams
   - See ARCHITECTURE_DIAGRAM.md
   - Go to https://mermaid.live/
   - Copy the Mermaid code and export as PNG

🔧 If you want to use this script:
1. Install Python library:
   pip install diagrams

2. Install Graphviz system package:
   - macOS: brew install graphviz
   - Linux: sudo apt-get install graphviz
   - Windows: Download from https://graphviz.org/download/

3. Run this script:
   python create_architecture_image.py
    """)
except Exception as e:
    print(f"Error: {e}")
    print("\nMake sure Graphviz is installed on your system")

