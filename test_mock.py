import pytest
from unittest.mock import MagicMock, patch
from agent import run_profile_agent
import json

@patch("agent.model")
@patch("scraper.DDGS")
def test_mock_pipeline(mock_ddgs, mock_model):
    # Mock Scraper
    mock_ddgs_instance = mock_ddgs.return_value.__enter__.return_value
    mock_ddgs_instance.text.return_value = [
        {"href": "https://www.upwork.com/freelancers/test", "body": "Experienced Python Developer"}
    ]

    # Mock Gemini
    mock_response = MagicMock()
    mock_response.text = json.dumps({
        "title": "Expert Python Developer",
        "overview": "I am an expert...",
        "skills": ["Python", "Django"],
        "rate": "$50/hr",
        "tips": ["Be concise"]
    })
    mock_model.generate_content.return_value = mock_response

    # Run Agent
    output = run_profile_agent("Python Developer", "5 years", ["Python"], "$50/hr", "Professional")
    
    # Verify
    assert "Expert Python Developer" in output
    assert "I am an expert" in output
