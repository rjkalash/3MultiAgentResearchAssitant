"""
Multi-Agent Research Assistant - Streamlit Web Interface
Interactive web UI for the research assistant
"""

import streamlit as st
from agents import run_research_assistant
import time


# Page configuration
st.set_page_config(
    page_title="Multi-Agent Research Assistant",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for premium styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .agent-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #667eea;
    }
    
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        border-radius: 8px;
        font-weight: 600;
        width: 100%;
        transition: transform 0.2s;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🔬 Multi-Agent Research Assistant</h1>
    <p style="font-size: 1.2rem; margin-top: 0.5rem;">
        Powered by LangGraph, Groq LPU (Llama-3-70b), and Tavily Search
    </p>
    <p style="font-size: 0.9rem; opacity: 0.9;">
        500+ tokens/sec inference • Real-time web search • Autonomous agentic workflow
    </p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("⚙️ Configuration")
    
    max_iterations = st.slider(
        "Max Research Iterations",
        min_value=1,
        max_value=5,
        value=2,
        help="Number of research-critique cycles before final summary"
    )
    
    st.markdown("---")
    
    st.header("🤖 Agent Workflow")
    st.markdown("""
    1. **Research Agent** 🔍
       - Searches web via Tavily API
       - Gathers real-time information
    
    2. **Critique Agent** 🔎
       - Evaluates research quality
       - Identifies gaps & biases
    
    3. **Summarize Agent** 📝
       - Synthesizes findings
       - Creates final response
    """)
    
    st.markdown("---")
    
    st.header("📊 Tech Stack")
    st.markdown("""
    - **LangGraph**: Agent orchestration
    - **Groq LPU**: Ultra-fast inference
    - **Tavily**: Real-time search
    - **Llama-3-70b**: Language model
    """)

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.header("💬 Ask Your Research Question")
    
    # Example queries
    example_queries = [
        "What are the latest developments in quantum computing?",
        "Compare the economic policies of major countries in 2025",
        "Explain recent breakthroughs in renewable energy",
        "What are the current trends in AI and machine learning?",
        "How is climate change affecting global agriculture?"
    ]
    
    selected_example = st.selectbox(
        "Or select an example query:",
        [""] + example_queries,
        index=0
    )
    
    query = st.text_area(
        "Enter your research question:",
        value=selected_example if selected_example else "",
        height=100,
        placeholder="e.g., What are the latest AI breakthroughs in 2025?"
    )
    
    col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
    
    with col_btn2:
        search_button = st.button("🚀 Start Research", use_container_width=True)

with col2:
    st.header("📈 Performance")
    
    st.markdown("""
    <div class="metric-card">
        <h3 style="color: #667eea; margin: 0;">500+</h3>
        <p style="margin: 0.5rem 0 0 0; color: #666;">Tokens/Second</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="metric-card" style="margin-top: 1rem;">
        <h3 style="color: #764ba2; margin: 0;">Real-Time</h3>
        <p style="margin: 0.5rem 0 0 0; color: #666;">Web Search</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="metric-card" style="margin-top: 1rem;">
        <h3 style="color: #667eea; margin: 0;">3 Agents</h3>
        <p style="margin: 0.5rem 0 0 0; color: #666;">Autonomous Workflow</p>
    </div>
    """, unsafe_allow_html=True)

# Process research request
if search_button and query:
    # Create tabs for different views
    tab1, tab2, tab3, tab4 = st.tabs(["📝 Summary", "🔍 Research", "🔎 Critique", "📊 Details"])
    
    with st.spinner("🤖 Agents are working on your query..."):
        start_time = time.time()
        
        # Progress tracking
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Run research assistant
        try:
            status_text.text("🔍 Research Agent: Searching for information...")
            progress_bar.progress(33)
            
            result = run_research_assistant(query, max_iterations=max_iterations)
            
            status_text.text("🔎 Critique Agent: Evaluating findings...")
            progress_bar.progress(66)
            
            time.sleep(0.5)  # Brief pause for UX
            
            status_text.text("📝 Summarize Agent: Creating final summary...")
            progress_bar.progress(100)
            
            end_time = time.time()
            elapsed_time = end_time - start_time
            
            # Clear progress indicators
            progress_bar.empty()
            status_text.empty()
            
            # Display success message
            st.success(f"✅ Research completed in {elapsed_time:.2f} seconds!")
            
            # Summary tab
            with tab1:
                st.markdown("### 📝 Final Summary")
                st.markdown(result["final_summary"])
            
            # Research tab
            with tab2:
                st.markdown("### 🔍 Research Findings")
                for i, research in enumerate(result["research_results"], 1):
                    with st.expander(f"Research Iteration {i}", expanded=(i == len(result["research_results"]))):
                        st.markdown(research)
            
            # Critique tab
            with tab3:
                st.markdown("### 🔎 Critique Feedback")
                for i, critique in enumerate(result["critique_feedback"], 1):
                    with st.expander(f"Critique Round {i}", expanded=(i == len(result["critique_feedback"]))):
                        st.markdown(critique)
            
            # Details tab
            with tab4:
                st.markdown("### 📊 Research Statistics")
                
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.metric("Iterations", result["iteration"])
                
                with col2:
                    st.metric("Research Rounds", len(result["research_results"]))
                
                with col3:
                    st.metric("Critique Rounds", len(result["critique_feedback"]))
                
                with col4:
                    st.metric("Time (sec)", f"{elapsed_time:.2f}")
                
                st.markdown("---")
                
                st.markdown("### 🔧 Configuration Used")
                st.json({
                    "query": query,
                    "max_iterations": max_iterations,
                    "model": "llama-3.1-70b-versatile",
                    "search_tool": "Tavily Search API",
                    "workflow": "LangGraph Multi-Agent"
                })
        
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.info("Please check your API keys in the .env file")

elif search_button and not query:
    st.warning("⚠️ Please enter a research question")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem 0;">
    <p>Built with LangGraph, Groq LPU, and Tavily Search API</p>
    <p style="font-size: 0.9rem;">Autonomous Agentic Workflow for Intelligent Research</p>
</div>
""", unsafe_allow_html=True)
