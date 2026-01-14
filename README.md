# Multi-Agent Research Assistant

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.2.28-green.svg)](https://github.com/langchain-ai/langgraph)
[![Groq](https://img.shields.io/badge/Groq-LPU-orange.svg)](https://groq.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An autonomous agentic workflow system built with **LangGraph**, **Groq LPU**, and **Tavily Search API** that decomposes complex user queries into specialized sub-tasks handled by dedicated AI agents.

## 🌟 Highlights

- 🤖 **Autonomous Multi-Agent System** with intelligent task decomposition
- ⚡ **500+ tokens/sec** inference speed using Groq's LPU technology
- 🔍 **Real-time web search** integration via Tavily API
- 🎯 **Reduced AI hallucinations** through live data retrieval
- 💻 **Premium Streamlit UI** with real-time progress tracking
- 🆓 **Free tier optimized** - works within Groq's 12,000 TPM limit

## 🚀 Features

### Autonomous Agentic Workflow
Uses **LangGraph** to orchestrate multiple specialized agents:
- **Research Agent** 🔍 - Gathers information using Tavily Search API
- **Critique Agent** 🔎 - Evaluates and validates research findings  
- **Summarize Agent** 📝 - Synthesizes information into coherent responses

### Ultra-Fast Inference
Leverages **Groq's LPU** with Llama-3.3-70b achieving:
- 500+ tokens per second
- Near-instant agent reasoning loops
- Optimized for production use

### Real-Time Web Search
Integrates **Tavily Search API** for:
- Up-to-date information retrieval
- Credible source analysis
- Reduced model hallucinations on current events

## 🏗️ Architecture

```
User Query
    ↓
Research Agent (Tavily Search + Groq Analysis)
    ↓
Critique Agent (Quality Evaluation)
    ↓
Decision: More Research Needed?
    ├─ Yes → Back to Research Agent
    └─ No → Summarize Agent
         ↓
    Final Response
```

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **LangGraph** | Agent orchestration and workflow management |
| **Groq LPU** | High-speed inference with Llama-3.3-70b |
| **Tavily API** | Real-time web search capabilities |
| **Python 3.9+** | Core programming language |
| **Streamlit** | Interactive web interface |

## 📋 Prerequisites

- Python 3.9 or higher
- Groq API Key ([Get it here](https://console.groq.com/))
- Tavily API Key ([Get it here](https://tavily.com/))

## 🔧 Installation

1. **Clone the repository**:
```bash
git clone https://github.com/rjkalash/3MultiAgentResearchAssitant.git
cd 3MultiAgentResearchAssitant
```

2. **Create a virtual environment**:
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Configure API keys**:

Create a `.env` file in the project root:
```env
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

## 🚀 Usage

### Quick Demo
```bash
python demo.py
```

### Command Line Interface
```bash
python main.py "What are the latest developments in quantum computing?"
```

### Streamlit Web Interface (Recommended)
```bash
streamlit run app.py
```
Then open your browser to `http://localhost:8501`

### Python API
```python
from agents import run_research_assistant

result = run_research_assistant(
    query="What are the latest AI breakthroughs in 2025?",
    max_iterations=2
)

print(result["final_summary"])
```

## 📊 Performance Metrics

| Metric | Value |
|--------|-------|
| **Inference Speed** | 500+ tokens/sec |
| **Response Time** | 10-30 seconds |
| **Token Efficiency** | ~7,000 TPM per query |
| **Accuracy** | High (real-time web data) |
| **Reliability** | Production-ready |

## 📝 Example Queries

Try these queries to test the system:

- "What are the latest AI breakthroughs in 2026?"
- "Compare renewable energy adoption across different continents"
- "Explain recent developments in quantum computing and their applications"
- "What are the current trends in cybersecurity?"
- "How is climate change affecting global agriculture?"

## 📚 Documentation

- **[SETUP.md](SETUP.md)** - Detailed installation and configuration guide
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - System design and technical details
- **[RATE_LIMITS.md](RATE_LIMITS.md)** - Token optimization and best practices
- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** - Quick reference card

## 🎯 Project Structure

```
multi-agent-research-assistant/
├── agents.py              # Core multi-agent system
├── app.py                 # Streamlit web interface
├── main.py                # CLI interface
├── demo.py                # Quick demo script
├── utils.py               # Utility functions
├── examples.py            # Usage examples
├── test_agents.py         # Test suite
├── requirements.txt       # Python dependencies
├── .env.example           # API keys template
└── docs/                  # Documentation files
```

## 🔑 API Keys

Get your free API keys:
- **Groq**: https://console.groq.com/keys
- **Tavily**: https://app.tavily.com/

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Raj Kalash Tiwari**

- GitHub: [@rjkalash](https://github.com/rjkalash)
- Project: [Multi-Agent Research Assistant](https://github.com/rjkalash/3MultiAgentResearchAssitant)

## 🙏 Acknowledgments

Built with:
- [LangGraph](https://github.com/langchain-ai/langgraph) - Agent orchestration framework
- [Groq](https://groq.com/) - Ultra-fast LPU inference
- [Tavily](https://tavily.com/) - Real-time web search API

## 📈 Project Status

✅ **Production Ready** - Fully functional and optimized for real-world use

---

**Star ⭐ this repository if you find it helpful!**
