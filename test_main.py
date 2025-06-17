# --- FILE: test_main.py ---
import json
import re
from agent import run_profile_agent
from schema import UpworkProfile
from evaluation import evaluate_quality

def extract_json(text):
    match = re.search(r"\{.*\}", text, re.DOTALL)
    return match.group(0) if match else None

def test_generated_profile_is_valid():
    user_input = {
        "role": "Web Developer",
        "experience": "3 years",
        "skills": ["React", "Tailwind", "Firebase"],
        "rate": "$25/hr",
        "tone": "Professional"
    }

    output = run_profile_agent(**user_input)
    json_text = extract_json(output)
    assert json_text is not None, "❌ Failed to extract JSON from output."

    data = json.loads(json_text)
    profile = UpworkProfile(**data)
    
    assert profile.title
    assert profile.overview
    assert isinstance(profile.skills, list)
    assert profile.hourly_rate.endswith("/hr")
    assert len(profile.profile_tips) >= 3

    evaluation = evaluate_quality(profile, user_input["skills"])
    print("✅ Matched:", evaluation["matched_keywords"])
    print("✅ Coverage:", round(evaluation["coverage"] * 100, 2), "%")
