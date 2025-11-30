# FitTelligence - Architecture Visualization

## 📸 Architecture Diagrams

This document contains visual representations of the FitTelligence multi-agent system architecture.

### View Diagrams

1. **Mermaid Diagrams** (renders on GitHub):
   - See `ARCHITECTURE_DIAGRAM.md` for interactive Mermaid diagrams
   - GitHub will automatically render these

2. **ASCII Art Diagram**:
   - See `ARCHITECTURE_DIAGRAM.txt` for text-based diagram
   - Can be viewed in any text editor

3. **Generate Image**:
   - Run `python create_architecture_image.py` (requires diagrams library)
   - Or use Mermaid Live Editor: https://mermaid.live/

---

## 🎨 Quick Image Generation

### Method 1: Mermaid Live Editor (Easiest)

1. Go to https://mermaid.live/
2. Copy the Mermaid code from `ARCHITECTURE_DIAGRAM.md`
3. Click "Export" → "PNG" or "SVG"
4. Download the image

### Method 2: GitHub Rendering

- Push the repository to GitHub
- View `ARCHITECTURE_DIAGRAM.md` in the browser
- GitHub will render the Mermaid diagrams automatically
- Take a screenshot

### Method 3: Python Script

```bash
# Install dependencies
pip install diagrams graphviz

# Install Graphviz system package
# macOS: brew install graphviz
# Linux: sudo apt-get install graphviz

# Generate image
python create_architecture_image.py
```

---

## 📊 Diagram Types Available

1. **Sequential Flow Diagram** - Shows how agents work in sequence
2. **Agent Relationship Diagram** - Shows agent-to-agent communication
3. **System Architecture Diagram** - Complete system overview
4. **Information Flow Diagram** - How data flows through the system

All diagrams are in `ARCHITECTURE_DIAGRAM.md` and can be rendered as images.

