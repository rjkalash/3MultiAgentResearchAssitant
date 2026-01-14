"""
Example usage of the Multi-Agent Research Assistant
Demonstrates various use cases and query types
"""

from agents import run_research_assistant


def example_1_current_events():
    """Example: Researching current events"""
    print("\n" + "="*80)
    print("EXAMPLE 1: Current Events Research")
    print("="*80)
    
    query = "What are the latest developments in artificial intelligence in 2025?"
    result = run_research_assistant(query, max_iterations=2)
    
    print("\n📝 SUMMARY:")
    print(result["final_summary"])


def example_2_comparative_analysis():
    """Example: Comparative analysis"""
    print("\n" + "="*80)
    print("EXAMPLE 2: Comparative Analysis")
    print("="*80)
    
    query = "Compare renewable energy adoption rates across different continents"
    result = run_research_assistant(query, max_iterations=2)
    
    print("\n📝 SUMMARY:")
    print(result["final_summary"])


def example_3_technical_topic():
    """Example: Technical topic research"""
    print("\n" + "="*80)
    print("EXAMPLE 3: Technical Topic")
    print("="*80)
    
    query = "Explain the latest breakthroughs in quantum computing and their practical applications"
    result = run_research_assistant(query, max_iterations=2)
    
    print("\n📝 SUMMARY:")
    print(result["final_summary"])


def example_4_market_trends():
    """Example: Market trends analysis"""
    print("\n" + "="*80)
    print("EXAMPLE 4: Market Trends")
    print("="*80)
    
    query = "What are the emerging trends in the electric vehicle market?"
    result = run_research_assistant(query, max_iterations=2)
    
    print("\n📝 SUMMARY:")
    print(result["final_summary"])


def run_all_examples():
    """Run all example queries"""
    examples = [
        example_1_current_events,
        example_2_comparative_analysis,
        example_3_technical_topic,
        example_4_market_trends
    ]
    
    for i, example in enumerate(examples, 1):
        print(f"\n\n{'#'*80}")
        print(f"Running Example {i}/{len(examples)}")
        print(f"{'#'*80}")
        example()
        
        if i < len(examples):
            input("\nPress Enter to continue to next example...")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        example_num = int(sys.argv[1])
        examples = [
            example_1_current_events,
            example_2_comparative_analysis,
            example_3_technical_topic,
            example_4_market_trends
        ]
        
        if 1 <= example_num <= len(examples):
            examples[example_num - 1]()
        else:
            print(f"Invalid example number. Choose 1-{len(examples)}")
    else:
        print("Usage: python examples.py [example_number]")
        print("\nAvailable examples:")
        print("  1. Current Events Research")
        print("  2. Comparative Analysis")
        print("  3. Technical Topic")
        print("  4. Market Trends")
        print("\nOr run: python examples.py (without arguments) to see usage")
