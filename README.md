# Multi-Agent Research Assistant

An autonomous agentic workflow system built with LangGraph, Groq LPU, and Tavily Search API that decomposes complex user queries into specialized sub-tasks handled by dedicated agents.

## 🚀 Features

- **Autonomous Agentic Workflow**: Uses LangGraph to orchestrate multiple specialized agents (Research, Critique, Summarize)
- **Ultra-Fast Inference**: Leverages Groq's LPU with Llama-3-70b achieving 500+ tokens/sec
- **Real-Time Web Search**: Integrates Tavily Search API for up-to-date information
- **Reduced Hallucinations**: Tool calling with live web data minimizes model hallucinations on current events
- **Intelligent Task Decomposition**: Automatically breaks down complex queries into manageable sub-tasks
- **Free Tier Optimized**: Configured to work within Groq's free tier rate limits (12,000 TPM)

## 🏗️ Architecture

The system uses a multi-agent architecture with three specialized agents:

1. **Research Agent**: Gathers information using Tavily Search API
2. **Critique Agent**: Evaluates and validates the research findings
3. **Summarize Agent**: Synthesizes information into coherent responses

## 🛠️ Tech Stack

- **LangGraph**: Agent orchestration and workflow management
- **Groq LPU**: High-speed inference with Llama-3-70b model
- **Tavily Search API**: Real-time web search capabilities
- **Python**: Core programming language
- **Streamlit**: Interactive web interface

## 📋 Prerequisites

- Python 3.9+
- Groq API Key
- Tavily API Key

## 🔧 Installation

1. Clone the repository:
```bash
cd multi-agent-research-assistant
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your API keys:
```env
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

## 🚀 Usage

### Command Line Interface

```bash
python main.py "What are the latest developments in quantum computing?"
```

### Streamlit Web Interface

```bash
streamlit run app.py
```

Then open your browser to `http://localhost:8501`

## 📊 Performance

- **Inference Speed**: 500+ tokens/sec with Groq LPU
- **Response Time**: Near-instant agent reasoning loops
- **Accuracy**: Reduced hallucinations through real-time web data

## 🔑 API Keys

Get your API keys from:
- Groq: https://console.groq.com/
- Tavily: https://tavily.com/

## 📝 Example Queries

- "What are the latest AI breakthroughs in 2025?"
- "Compare the economic policies of major countries"
- "Explain recent developments in renewable energy"
- "What are the current trends in cybersecurity?"

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

MIT License

## 👤 Author

Built with ❤️ using LangGraph, Groq, and Tavily
