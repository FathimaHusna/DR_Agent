# --- FILE: main.py ---
import json
import re
from schema import UpworkProfile
from agent import run_profile_agent
from evaluation import evaluate_quality
from validation import validate_inputs


def extract_json(text):
    match = re.search(r"\{.*\}", text, re.DOTALL)
    return match.group(0) if match else None

def main():
    user_input = {
        "role": "Python Developer",
        "experience": "2 years",
        "skills": ["Selenium", "Web Scraping", "Automation"],
        "rate": "$15/hr",
        "tone": "Professional"
    }

    errors = validate_inputs(
        user_input['role'],
        user_input['experience'],
        user_input['skills'],
        user_input['rate'],
        user_input['tone']
    )
    if errors:
        for err in errors:
            print(f"❌ {err}")
        return

    profile_text = run_profile_agent(**user_input)
    json_text = extract_json(profile_text)

    if not json_text:
        print("❌ Failed to extract JSON.")
        print(profile_text)
        return

    parsed = json.loads(json_text)
    profile = UpworkProfile(**parsed)
    print("\n✅ Profile Generated:\n")
    print(profile.model_dump_json(indent=2))

    keywords = [kw for kw in user_input['skills']]  # Dynamic keyword extraction
    quality = evaluate_quality(profile, keywords)
    print("\n🔍 Keyword Evaluation:")
    print(f"Matched: {quality['matched_keywords']}")
    print(f"Coverage: {quality['coverage'] * 100:.2f}%")


if __name__ == "__main__":
    main()
