"""
Tests for the Multi-Agent Research Assistant
Run with: python -m pytest test_agents.py
"""

import pytest
from unittest.mock import Mock, patch
from agents import AgentState, ResearchAgent, CritiqueAgent, SummarizeAgent, should_continue


class TestAgentState:
    """Test the AgentState structure"""
    
    def test_initial_state(self):
        """Test initial state creation"""
        state = {
            "query": "Test query",
            "research_results": [],
            "critique_feedback": [],
            "final_summary": "",
            "iteration": 0,
            "max_iterations": 2
        }
        
        assert state["query"] == "Test query"
        assert len(state["research_results"]) == 0
        assert state["iteration"] == 0


class TestResearchAgent:
    """Test the Research Agent"""
    
    @patch('agents.tavily_search')
    @patch('agents.llm')
    def test_research_execution(self, mock_llm, mock_search):
        """Test research agent execution"""
        # Mock search results
        mock_search.invoke.return_value = [
            {"content": "Test result 1"},
            {"content": "Test result 2"}
        ]
        
        # Mock LLM response
        mock_response = Mock()
        mock_response.content = "Research summary"
        mock_llm.invoke.return_value = mock_response
        
        # Create agent and state
        agent = ResearchAgent(mock_llm, mock_search)
        state = {
            "query": "Test query",
            "research_results": [],
            "critique_feedback": [],
            "final_summary": "",
            "iteration": 0,
            "max_iterations": 2
        }
        
        # Execute
        result = agent.execute(state)
        
        # Assertions
        assert len(result["research_results"]) == 1
        assert result["iteration"] == 1
        assert "Research summary" in result["research_results"]


class TestCritiqueAgent:
    """Test the Critique Agent"""
    
    @patch('agents.llm')
    def test_critique_execution(self, mock_llm):
        """Test critique agent execution"""
        # Mock LLM response
        mock_response = Mock()
        mock_response.content = "Critique feedback"
        mock_llm.invoke.return_value = mock_response
        
        # Create agent and state
        agent = CritiqueAgent(mock_llm)
        state = {
            "query": "Test query",
            "research_results": ["Research result"],
            "critique_feedback": [],
            "final_summary": "",
            "iteration": 1,
            "max_iterations": 2
        }
        
        # Execute
        result = agent.execute(state)
        
        # Assertions
        assert len(result["critique_feedback"]) == 1
        assert "Critique feedback" in result["critique_feedback"]


class TestSummarizeAgent:
    """Test the Summarize Agent"""
    
    @patch('agents.llm')
    def test_summarize_execution(self, mock_llm):
        """Test summarize agent execution"""
        # Mock LLM response
        mock_response = Mock()
        mock_response.content = "Final summary"
        mock_llm.invoke.return_value = mock_response
        
        # Create agent and state
        agent = SummarizeAgent(mock_llm)
        state = {
            "query": "Test query",
            "research_results": ["Research result"],
            "critique_feedback": ["Critique feedback"],
            "final_summary": "",
            "iteration": 1,
            "max_iterations": 2
        }
        
        # Execute
        result = agent.execute(state)
        
        # Assertions
        assert result["final_summary"] == "Final summary"


class TestWorkflowLogic:
    """Test workflow decision logic"""
    
    def test_should_continue_max_iterations(self):
        """Test that workflow stops at max iterations"""
        state = {
            "query": "Test",
            "research_results": [],
            "critique_feedback": [],
            "final_summary": "",
            "iteration": 2,
            "max_iterations": 2
        }
        
        result = should_continue(state)
        assert result == "summarize"
    
    def test_should_continue_needs_research(self):
        """Test that workflow continues if more research needed"""
        state = {
            "query": "Test",
            "research_results": [],
            "critique_feedback": ["More research needed"],
            "final_summary": "",
            "iteration": 1,
            "max_iterations": 3
        }
        
        result = should_continue(state)
        assert result == "research"
    
    def test_should_continue_ready_for_summary(self):
        """Test that workflow proceeds to summary when ready"""
        state = {
            "query": "Test",
            "research_results": [],
            "critique_feedback": ["Looks good"],
            "final_summary": "",
            "iteration": 1,
            "max_iterations": 3
        }
        
        result = should_continue(state)
        assert result == "summarize"


class TestUtils:
    """Test utility functions"""
    
    def test_validate_api_keys(self):
        """Test API key validation"""
        from utils import validate_api_keys
        
        # This will check actual environment
        validation = validate_api_keys()
        
        assert isinstance(validation, dict)
        assert "groq" in validation
        assert "tavily" in validation


if __name__ == "__main__":
    # Run tests
    pytest.main([__file__, "-v"])
