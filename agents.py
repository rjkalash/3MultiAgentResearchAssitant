"""
Multi-Agent Research Assistant Configuration
Defines the state, agents, and workflow for the research system
"""

from typing import TypedDict, Annotated, List
from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import operator
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq LLM with Llama-3-70b for ultra-fast inference (500+ tokens/sec)
# Optimized for free tier rate limits (12,000 TPM)
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=1024,  # Reduced to stay within rate limits
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# Initialize Tavily Search for real-time web data
# Reduced results to minimize token usage
tavily_search = TavilySearchResults(
    max_results=3,  # Reduced from 5 to stay within rate limits
    tavily_api_key=os.getenv("TAVILY_API_KEY")
)


class AgentState(TypedDict):
    """
    State shared across all agents in the workflow
    """
    query: str
    research_results: Annotated[List[str], operator.add]
    critique_feedback: Annotated[List[str], operator.add]
    final_summary: str
    iteration: int
    max_iterations: int


class ResearchAgent:
    """
    Research Agent: Gathers information using Tavily Search API
    Responsible for finding relevant, up-to-date information
    """
    
    def __init__(self, llm, search_tool):
        self.llm = llm
        self.search_tool = search_tool
    
    def execute(self, state: AgentState) -> AgentState:
        """
        Execute research by searching the web and analyzing results
        """
        query = state["query"]
        
        print(f"\n🔍 Research Agent: Searching for information about '{query}'...")
        
        # Perform web search using Tavily
        search_results = self.search_tool.invoke(query)
        
        # Use LLM to analyze and extract key information
        system_prompt = """You are a research specialist. Analyze the search results and extract 
        the most relevant and accurate information. Focus on facts, recent developments, and credible sources.
        Be concise but comprehensive."""
        
        # Truncate content to prevent token overflow (max ~500 chars per source)
        research_context = "\n\n".join([
            f"Source {i+1}: {result.get('content', '')[:500]}..."
            for i, result in enumerate(search_results)
        ])
        
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=f"Query: {query}\n\nSearch Results:\n{research_context}\n\nProvide a detailed research summary:")
        ]
        
        response = self.llm.invoke(messages)
        research_summary = response.content
        
        print(f"✅ Research completed: {len(research_summary)} characters")
        
        state["research_results"].append(research_summary)
        state["iteration"] += 1
        
        return state


class CritiqueAgent:
    """
    Critique Agent: Evaluates and validates research findings
    Identifies gaps, inconsistencies, or areas needing more research
    """
    
    def __init__(self, llm):
        self.llm = llm
    
    def execute(self, state: AgentState) -> AgentState:
        """
        Critique the research findings and provide feedback
        """
        query = state["query"]
        research = state["research_results"][-1] if state["research_results"] else ""
        
        # Truncate research to prevent token overflow
        research_truncated = research[:1000] if len(research) > 1000 else research
        
        print(f"\n🔎 Critique Agent: Evaluating research quality...")
        
        system_prompt = """You are a critical analyst. Briefly evaluate the research for accuracy, completeness, and relevance. Be concise."""
        
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=f"Query: {query}\n\nResearch:\n{research_truncated}\n\nProvide brief critique:")
        ]
        
        response = self.llm.invoke(messages)
        critique = response.content
        
        print(f"✅ Critique completed")
        
        state["critique_feedback"].append(critique)
        
        return state


class SummarizeAgent:
    """
    Summarize Agent: Synthesizes research and critique into final response
    Creates a coherent, comprehensive answer to the user's query
    """
    
    def __init__(self, llm):
        self.llm = llm
    
    def execute(self, state: AgentState) -> AgentState:
        """
        Create final summary incorporating research and critique
        """
        query = state["query"]
        research = "\n\n".join(state["research_results"])
        critique = "\n\n".join(state["critique_feedback"])
        
        # Truncate to prevent token overflow
        research_truncated = research[:1500] if len(research) > 1500 else research
        critique_truncated = critique[:500] if len(critique) > 500 else critique
        
        print(f"\n📝 Summarize Agent: Creating final summary...")
        
        system_prompt = """You are a synthesis expert. Create a clear, well-structured response that directly answers the query using the research findings."""
        
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=f"""Query: {query}

Research:
{research_truncated}

Critique:
{critique_truncated}

Create final response:""")
        ]
        
        response = self.llm.invoke(messages)
        summary = response.content
        
        print(f"✅ Summary completed: {len(summary)} characters")
        
        state["final_summary"] = summary
        
        return state


def should_continue(state: AgentState) -> str:
    """
    Decide whether to continue research or move to summarization
    """
    if state["iteration"] >= state["max_iterations"]:
        return "summarize"
    
    # Check if critique suggests more research is needed
    if state["critique_feedback"]:
        last_critique = state["critique_feedback"][-1].lower()
        if "more research" in last_critique or "insufficient" in last_critique or "gap" in last_critique:
            if state["iteration"] < state["max_iterations"]:
                return "research"
    
    return "summarize"


def create_research_workflow():
    """
    Create the LangGraph workflow with all agents
    """
    # Initialize agents
    research_agent = ResearchAgent(llm, tavily_search)
    critique_agent = CritiqueAgent(llm)
    summarize_agent = SummarizeAgent(llm)
    
    # Create workflow graph
    workflow = StateGraph(AgentState)
    
    # Add nodes for each agent
    workflow.add_node("research", research_agent.execute)
    workflow.add_node("critique", critique_agent.execute)
    workflow.add_node("summarize", summarize_agent.execute)
    
    # Define edges
    workflow.set_entry_point("research")
    workflow.add_edge("research", "critique")
    workflow.add_conditional_edges(
        "critique",
        should_continue,
        {
            "research": "research",
            "summarize": "summarize"
        }
    )
    workflow.add_edge("summarize", END)
    
    return workflow.compile()


def run_research_assistant(query: str, max_iterations: int = 2) -> dict:
    """
    Run the multi-agent research assistant on a query
    
    Args:
        query: The user's research question
        max_iterations: Maximum number of research-critique cycles
    
    Returns:
        Final state with research results and summary
    """
    print(f"\n{'='*80}")
    print(f"🚀 Multi-Agent Research Assistant")
    print(f"{'='*80}")
    print(f"Query: {query}")
    print(f"{'='*80}\n")
    
    # Create workflow
    app = create_research_workflow()
    
    # Initialize state
    initial_state = {
        "query": query,
        "research_results": [],
        "critique_feedback": [],
        "final_summary": "",
        "iteration": 0,
        "max_iterations": max_iterations
    }
    
    # Run the workflow
    final_state = app.invoke(initial_state)
    
    print(f"\n{'='*80}")
    print(f"✨ Research Complete!")
    print(f"{'='*80}\n")
    
    return final_state
