import json
from schema import UpworkProfile
from agent import run_profile_agent

import re

def extract_json(text):
    """Extract JSON block from LLM output."""
    match = re.search(r"\{.*\}", text, re.DOTALL)
    return match.group(0) if match else None

def test_valid_json_response():
    output = run_profile_agent("Python Developer", "2 years", ["Selenium"], "$15/hr", "Friendly")
    cleaned_output = extract_json(output)
    assert cleaned_output, "❌ No JSON object found in output."

    parsed = json.loads(cleaned_output)
    profile = UpworkProfile(**parsed)

    assert profile.title
    assert isinstance(profile.skills, list)
    assert profile.hourly_rate.endswith("/hr")

