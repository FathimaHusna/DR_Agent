import json
import re
from schema import UpworkProfile
from agent import run_profile_agent

def extract_json(text):
    """Extracts the first JSON object from raw Gemini output (removes markdown, etc.)"""
    match = re.search(r"\{.*\}", text, re.DOTALL)
    return match.group(0) if match else None

def main():
    role = "Python Developer"
    experience = "2 years"
    skills = ["Selenium", "Web Scraping", "Automation"]
    rate = "$15/hr"

    raw_output = run_profile_agent(role, experience, skills, rate)
    cleaned_output = extract_json(raw_output)

    if not cleaned_output:
        print("❌ Failed to extract JSON from output.")
        print("Raw Output:\n", raw_output)
        return

    try:
        parsed = json.loads(cleaned_output)

        # Auto-correct hourly_rate if it's numeric
        if isinstance(parsed.get("hourly_rate"), (int, float)):
            parsed["hourly_rate"] = f"${parsed['hourly_rate']}/hr"

        profile = UpworkProfile(**parsed)
        print("✅ Valid profile generated:\n")
        print(profile.model_dump_json(indent=2))

    except Exception as e:
        print("❌ Validation error:", e)
        print("\nCleaned Output:\n", cleaned_output)


if __name__ == "__main__":
    main()
