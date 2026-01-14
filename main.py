"""
Multi-Agent Research Assistant - Command Line Interface
Run research queries from the command line
"""

import sys
from agents import run_research_assistant


def main():
    """
    Main CLI entry point
    """
    if len(sys.argv) < 2:
        print("Usage: python main.py \"Your research question here\"")
        print("\nExample:")
        print('  python main.py "What are the latest developments in quantum computing?"')
        sys.exit(1)
    
    # Get query from command line arguments
    query = " ".join(sys.argv[1:])
    
    # Run the research assistant
    result = run_research_assistant(query, max_iterations=2)
    
    # Display results
    print("\n" + "="*80)
    print("📊 FINAL SUMMARY")
    print("="*80 + "\n")
    print(result["final_summary"])
    print("\n" + "="*80)
    print(f"📈 Statistics:")
    print(f"  - Research iterations: {result['iteration']}")
    print(f"  - Research findings: {len(result['research_results'])}")
    print(f"  - Critique rounds: {len(result['critique_feedback'])}")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()
