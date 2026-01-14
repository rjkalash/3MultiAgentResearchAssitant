# Quick Reference Card

## 🚀 Quick Start

```bash
# Run demo
python demo.py

# Run web interface
python -m streamlit run app.py

# Run CLI
python main.py "Your question here"
```

## 📊 System Status

✅ **OPERATIONAL** - Optimized for Groq free tier
- Token usage: ~7,000 per iteration
- Rate limit: 12,000 TPM (safe)
- Search results: 3 per query
- Max tokens: 1024 per response

## 🎯 Current Configuration

| Setting | Value | Purpose |
|---------|-------|---------|
| Model | llama-3.3-70b-versatile | Ultra-fast inference |
| Max Tokens | 1024 | Stay within rate limits |
| Search Results | 3 | Reduce token usage |
| Max Iterations | 2 | Balance quality/speed |
| Content Truncation | Yes | Prevent overflow |

## 📝 Example Queries

**Simple** (Fast):
```bash
python main.py "What is AI?"
```

**Medium** (Balanced):
```bash
python main.py "Explain quantum computing"
```

**Complex** (Thorough):
```bash
python main.py "What are the latest developments in renewable energy?"
```

## 🔧 Troubleshooting

### Rate Limit Error (413)
✅ **FIXED** - System optimized
If you still see it:
1. Wait 60 seconds
2. Reduce iterations to 1
3. Use shorter queries

### Import Errors
```bash
pip install -r requirements.txt
```

### API Key Errors
Check `.env` file has:
```
GROQ_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
```

## 📚 Documentation

- `README.md` - Overview
- `SETUP.md` - Installation guide
- `ARCHITECTURE.md` - System design
- `RATE_LIMITS.md` - Token optimization
- `FIX_SUMMARY.md` - Recent fixes
- `PROJECT_SUMMARY.md` - Complete summary

## 🎓 Key Files

| File | Purpose |
|------|---------|
| `agents.py` | Core multi-agent system |
| `app.py` | Streamlit web interface |
| `main.py` | CLI interface |
| `demo.py` | Quick test script |
| `utils.py` | Helper functions |
| `examples.py` | Usage examples |

## 💡 Tips

1. **Keep queries concise** for faster results
2. **Use max_iterations=1** for quick answers
3. **Save results** using `utils.py` functions
4. **Monitor usage** at console.groq.com
5. **Upgrade to Dev tier** for heavy use

## 🌐 URLs

- Groq Console: https://console.groq.com/
- Tavily Dashboard: https://app.tavily.com/
- Web Interface: http://localhost:8501

## 📈 Performance

- **Speed**: 500+ tokens/sec
- **Latency**: 10-30 seconds per query
- **Reliability**: High (optimized for free tier)
- **Quality**: Excellent (real-time web data)

## ✨ Features

✅ Autonomous agent workflow
✅ Real-time web search
✅ Ultra-fast inference
✅ Reduced hallucinations
✅ Premium web UI
✅ CLI & Python API
✅ Free tier compatible

## 🎯 Resume Highlights

- Architected autonomous agentic workflow with LangGraph
- Leveraged Groq LPU (500+ tokens/sec)
- Implemented tool calling with Tavily Search API
- Optimized for production use on free tier

---

**Status**: ✅ PRODUCTION READY
**Last Updated**: January 15, 2026
