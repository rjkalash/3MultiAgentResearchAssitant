# Multi-Agent Research Assistant - Architecture

## System Overview

The Multi-Agent Research Assistant is an autonomous agentic workflow system that decomposes complex research queries into specialized sub-tasks handled by dedicated agents.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                     User Query Input                         │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   LangGraph Workflow                         │
│                                                               │
│  ┌───────────────┐      ┌───────────────┐                   │
│  │   Research    │──────▶│   Critique    │                   │
│  │     Agent     │      │     Agent     │                   │
│  │               │      │               │                   │
│  │ • Tavily      │      │ • Validates   │                   │
│  │   Search      │      │ • Identifies  │                   │
│  │ • Groq LPU    │      │   gaps        │                   │
│  │ • 500+ tok/s  │      │ • Provides    │                   │
│  │               │      │   feedback    │                   │
│  └───────────────┘      └───────┬───────┘                   │
│         ▲                        │                           │
│         │                        │                           │
│         │        Need more       │                           │
│         └────────research?───────┘                           │
│                     │                                        │
│                     │ Ready for summary                      │
│                     ▼                                        │
│              ┌───────────────┐                               │
│              │  Summarize    │                               │
│              │    Agent      │                               │
│              │               │                               │
│              │ • Synthesizes │                               │
│              │ • Formats     │                               │
│              │ • Finalizes   │                               │
│              └───────────────┘                               │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   Final Response                             │
└─────────────────────────────────────────────────────────────┘
```

## Component Details

### 1. Research Agent
**Purpose**: Gather real-time information from the web

**Capabilities**:
- Executes web searches via Tavily Search API
- Retrieves up to 5 relevant sources per query
- Uses Groq LPU (Llama-3-70b) for analysis
- Achieves 500+ tokens/sec inference speed
- Extracts key information from search results

**Tools**:
- Tavily Search API (real-time web search)
- Groq LPU (ultra-fast inference)

### 2. Critique Agent
**Purpose**: Evaluate research quality and identify gaps

**Capabilities**:
- Validates accuracy and credibility
- Identifies information gaps
- Checks for biases or missing perspectives
- Assesses recency and relevance
- Provides constructive feedback

**Decision Logic**:
- If gaps found → trigger another research iteration
- If quality sufficient → proceed to summarization
- Max iterations limit prevents infinite loops

### 3. Summarize Agent
**Purpose**: Synthesize findings into coherent response

**Capabilities**:
- Combines all research findings
- Incorporates critique feedback
- Creates well-structured response
- Ensures clarity and comprehensiveness
- Formats for user consumption

## State Management

The system uses a shared state object that flows through all agents:

```python
class AgentState(TypedDict):
    query: str                    # Original user query
    research_results: List[str]   # Accumulated research findings
    critique_feedback: List[str]  # Critique evaluations
    final_summary: str            # Final synthesized response
    iteration: int                # Current iteration count
    max_iterations: int           # Maximum allowed iterations
```

## Workflow Logic

### Entry Point
1. User submits query
2. Initialize state with query and parameters
3. Enter workflow at Research Agent

### Research-Critique Loop
1. **Research Agent** searches and analyzes
2. **Critique Agent** evaluates findings
3. **Decision Point**:
   - If gaps identified AND iterations < max → return to Research
   - Otherwise → proceed to Summarize

### Exit Point
1. **Summarize Agent** creates final response
2. Return complete state to user
3. Display summary and metadata

## Performance Characteristics

### Speed
- **Inference**: 500+ tokens/sec (Groq LPU)
- **Search**: Real-time web results (Tavily)
- **Total**: Typically 10-30 seconds per query

### Accuracy
- **Reduced Hallucinations**: Real-time web data
- **Multi-perspective**: Multiple sources analyzed
- **Validated**: Critique agent ensures quality

### Scalability
- **Parallel Processing**: Agents can run concurrently
- **Configurable**: Adjustable iteration limits
- **Extensible**: Easy to add new agents

## Technology Stack

### Core Framework
- **LangGraph**: Agent orchestration and workflow
- **LangChain**: LLM integration and tooling

### AI/ML Services
- **Groq LPU**: Ultra-fast inference engine
- **Llama-3-70b**: Large language model
- **Tavily API**: Real-time web search

### Development
- **Python 3.9+**: Core language
- **Streamlit**: Web interface
- **python-dotenv**: Configuration management

## Extension Points

### Adding New Agents
1. Create agent class with `execute(state)` method
2. Add node to workflow graph
3. Define edges and transitions
4. Update state schema if needed

### Custom Tools
1. Implement tool using LangChain format
2. Integrate into relevant agent
3. Update agent prompts to use tool

### Alternative Models
1. Replace Groq with other LLM provider
2. Update initialization in `agents.py`
3. Adjust prompts for model characteristics

## Security Considerations

- API keys stored in `.env` file (not committed)
- Input validation on user queries
- Rate limiting on external API calls
- Error handling for API failures

## Future Enhancements

1. **Memory System**: Remember previous queries
2. **Source Citations**: Link to original sources
3. **Multi-modal**: Support images, videos
4. **Collaborative**: Multiple users, shared research
5. **Export**: PDF, markdown, JSON outputs
