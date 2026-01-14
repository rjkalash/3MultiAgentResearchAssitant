"""
Quick Demo - Multi-Agent Research Assistant
A simple demonstration of the research assistant
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

print("="*80)
print("🔬 Multi-Agent Research Assistant - Quick Demo")
print("="*80)

# Check API keys
groq_key = os.getenv("GROQ_API_KEY")
tavily_key = os.getenv("TAVILY_API_KEY")

print("\n📋 Configuration Check:")
print(f"  Groq API Key:   {'✅ Configured' if groq_key and len(groq_key) > 20 else '❌ Missing'}")
print(f"  Tavily API Key: {'✅ Configured' if tavily_key and len(tavily_key) > 20 else '❌ Missing'}")

if not (groq_key and tavily_key):
    print("\n❌ Error: API keys not configured properly")
    print("Please check your .env file")
    exit(1)

print("\n🚀 Starting research assistant...")
print("Query: 'What are the latest developments in AI?'")
print("\nThis will demonstrate:")
print("  1. Research Agent - Searching web via Tavily")
print("  2. Critique Agent - Evaluating findings")
print("  3. Summarize Agent - Creating final summary")
print("\n" + "="*80)

try:
    from agents import run_research_assistant
    
    # Run a simple query
    result = run_research_assistant(
        query="What are the latest developments in AI?",
        max_iterations=1  # Keep it quick for demo
    )
    
    print("\n" + "="*80)
    print("✨ DEMO COMPLETE!")
    print("="*80)
    print("\n📝 Final Summary:")
    print("-" * 80)
    print(result["final_summary"])
    print("-" * 80)
    
    print(f"\n📊 Statistics:")
    print(f"  - Iterations: {result['iteration']}")
    print(f"  - Research rounds: {len(result['research_results'])}")
    print(f"  - Critique rounds: {len(result['critique_feedback'])}")
    
    print("\n" + "="*80)
    print("✅ Demo successful! The multi-agent system is working.")
    print("\nNext steps:")
    print("  - Run 'streamlit run app.py' for the web interface")
    print("  - Run 'python main.py \"your query\"' for CLI usage")
    print("  - Check examples.py for more query examples")
    print("="*80)

except ImportError as e:
    print(f"\n❌ Import Error: {e}")
    print("\nPlease ensure all dependencies are installed:")
    print("  pip install -r requirements.txt")
except Exception as e:
    print(f"\n❌ Error: {e}")
    print("\nPlease check your API keys and internet connection")
