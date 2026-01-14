# Setup Guide - Multi-Agent Research Assistant

## Quick Start

### 1. Prerequisites

Ensure you have the following installed:
- Python 3.9 or higher
- pip (Python package manager)
- Git (for version control)

### 2. Get API Keys

You'll need API keys from two services:

#### Groq API Key
1. Visit https://console.groq.com/
2. Sign up for a free account
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key (you won't see it again!)

**Features**:
- Ultra-fast inference with LPU technology
- 500+ tokens/sec with Llama-3-70b
- Free tier available

#### Tavily API Key
1. Visit https://tavily.com/
2. Sign up for an account
3. Go to your dashboard
4. Find your API key
5. Copy the key

**Features**:
- Real-time web search
- Optimized for AI applications
- Free tier includes 1000 searches/month

### 3. Installation

```bash
# Clone or navigate to the project directory
cd multi-agent-research-assistant

# Create a virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 4. Configuration

Create a `.env` file in the project root:

```bash
# Copy the example file
copy .env.example .env  # Windows
# or
cp .env.example .env    # macOS/Linux
```

Edit `.env` and add your API keys:

```env
GROQ_API_KEY=gsk_your_actual_groq_api_key_here
TAVILY_API_KEY=tvly-your_actual_tavily_api_key_here
```

**Important**: Never commit the `.env` file to version control!

### 5. Verify Installation

Test that everything is working:

```bash
python -c "from agents import run_research_assistant; print('✅ Installation successful!')"
```

## Usage

### Command Line Interface

Run a single query:

```bash
python main.py "What are the latest developments in quantum computing?"
```

### Web Interface (Recommended)

Launch the Streamlit app:

```bash
streamlit run app.py
```

Then open your browser to: http://localhost:8501

### Python API

Use in your own Python scripts:

```python
from agents import run_research_assistant

result = run_research_assistant(
    query="Your research question here",
    max_iterations=2
)

print(result["final_summary"])
```

## Configuration Options

### Max Iterations

Control how many research-critique cycles to perform:

```python
# Quick research (1 iteration)
result = run_research_assistant(query, max_iterations=1)

# Thorough research (3 iterations)
result = run_research_assistant(query, max_iterations=3)
```

**Recommendations**:
- Simple queries: 1-2 iterations
- Complex queries: 2-3 iterations
- Deep research: 3-5 iterations

### Model Selection

To use a different Groq model, edit `agents.py`:

```python
llm = ChatGroq(
    model="llama-3.1-70b-versatile",  # Change this
    temperature=0.7,
    max_tokens=2048,
    groq_api_key=os.getenv("GROQ_API_KEY")
)
```

Available models:
- `llama-3.1-70b-versatile` (recommended, fastest)
- `llama-3.1-8b-instant` (faster, less capable)
- `mixtral-8x7b-32768` (alternative)

## Troubleshooting

### API Key Errors

**Error**: `AuthenticationError: Invalid API key`

**Solution**:
1. Check that `.env` file exists
2. Verify API keys are correct (no extra spaces)
3. Ensure `.env` is in the project root directory

### Import Errors

**Error**: `ModuleNotFoundError: No module named 'langgraph'`

**Solution**:
```bash
# Ensure virtual environment is activated
# Reinstall dependencies
pip install -r requirements.txt
```

### Streamlit Issues

**Error**: `streamlit: command not found`

**Solution**:
```bash
# Install streamlit explicitly
pip install streamlit

# Or reinstall all dependencies
pip install -r requirements.txt
```

### Rate Limiting

**Error**: `RateLimitError` from Groq or Tavily

**Solution**:
- Wait a few minutes before retrying
- Reduce max_iterations
- Check your API usage limits
- Consider upgrading to paid tier

## Performance Tips

### Optimize Speed

1. **Use faster models** for simple queries:
   ```python
   model="llama-3.1-8b-instant"
   ```

2. **Reduce iterations** for quick answers:
   ```python
   max_iterations=1
   ```

3. **Limit search results** in `agents.py`:
   ```python
   tavily_search = TavilySearchResults(max_results=3)
   ```

### Improve Quality

1. **Increase iterations** for complex topics:
   ```python
   max_iterations=3
   ```

2. **Use larger models**:
   ```python
   model="llama-3.1-70b-versatile"
   ```

3. **Adjust temperature** for more focused responses:
   ```python
   temperature=0.5  # More focused
   temperature=0.9  # More creative
   ```

## Advanced Usage

### Custom Agents

Add your own specialized agent:

```python
class FactCheckAgent:
    def __init__(self, llm):
        self.llm = llm
    
    def execute(self, state: AgentState) -> AgentState:
        # Your custom logic here
        return state
```

### Workflow Modification

Customize the agent workflow in `agents.py`:

```python
workflow.add_node("factcheck", factcheck_agent.execute)
workflow.add_edge("critique", "factcheck")
workflow.add_edge("factcheck", "summarize")
```

### Export Results

Save results to file:

```python
import json

result = run_research_assistant(query)

with open("research_output.json", "w") as f:
    json.dump(result, f, indent=2)
```

## Best Practices

1. **Start Simple**: Begin with 1-2 iterations
2. **Specific Queries**: More specific = better results
3. **Monitor Usage**: Track API usage to avoid limits
4. **Cache Results**: Save expensive queries
5. **Error Handling**: Always wrap in try-except

## Getting Help

- Check the [ARCHITECTURE.md](ARCHITECTURE.md) for system details
- Review [examples.py](examples.py) for usage patterns
- Open an issue on GitHub for bugs
- Read API documentation:
  - [Groq Docs](https://console.groq.com/docs)
  - [Tavily Docs](https://docs.tavily.com/)
  - [LangGraph Docs](https://langchain-ai.github.io/langgraph/)

## Next Steps

1. Try the example queries in `examples.py`
2. Experiment with different max_iterations
3. Customize agent prompts for your use case
4. Build your own agents for specialized tasks
5. Integrate into your applications

Happy researching! 🔬
