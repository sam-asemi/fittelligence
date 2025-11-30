# Quick Start Guide

## 🚀 Get Started in 3 Steps

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set API Key

```bash
export GOOGLE_API_KEY="your-api-key-here"
```

Or create a `.env` file:
```bash
echo "GOOGLE_API_KEY=your-api-key-here" > .env
```

### 3. Run Demo

```bash
python demo.py
```

**Interactive Mode:**
- The demo will prompt you to enter client information interactively
- Or choose to use demo data for quick testing
- All information is collected through the terminal

That's it! The demo will show all 5 agents working sequentially with your input.

---

## 📚 Documentation Quick Links

- **[README.md](README.md)** - Full project documentation
- **[SUBMISSION_WRITEUP.md](SUBMISSION_WRITEUP.md)** - Kaggle submission document
- **[KAGGLE_SUBMISSION.md](KAGGLE_SUBMISSION.md)** - Technical details
- **[SUBMISSION_SUMMARY.md](SUBMISSION_SUMMARY.md)** - Final submission checklist

---

## 🎯 What You'll See

The demo runs through a complete sequential agent workflow:

1. **Reception Agent** - Collects client information
2. **Body Scanner Agent** - Analyzes body and movement
3. **PT Agent** - Creates training plan
4. **Nutrition Agent** - Creates nutrition plan
5. **Head Coach Agent** - Integrates everything

Each agent receives context from previous agents and passes information forward.

---

## ⚠️ Troubleshooting

**Error: "API credentials not configured"**
- Make sure you've set `GOOGLE_API_KEY` environment variable
- Or created a `.env` file with your API key

**Error: "Module not found"**
- Run `pip install -r requirements.txt`
- Make sure you're in the project directory

**No response from agents**
- Check that your API key is valid
- Verify API key format: should start with "AIza"
- Check internet connection (Google Search requires internet)

---

## 📞 Need Help?

- Review `README.md` for detailed documentation
- Check `FINAL_CHECKLIST.md` for submission verification
- See `SUBMISSION_SUMMARY.md` for submission steps

---

**Ready to submit?** Check `SUBMISSION_SUMMARY.md` for next steps!

