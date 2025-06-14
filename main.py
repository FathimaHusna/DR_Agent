import json
from schema import UpworkProfile
from agent import run_profile_agent

def main():
    role = "Python Developer"
    experience = "2 years"
    skills = ["Selenium", "Web Scraping", "Automation"]
    rate = "$15/hr"

    raw_output = run_profile_agent(role, experience, skills, rate)

    try:
        parsed = json.loads(raw_output)
        profile = UpworkProfile(**parsed)
        print("✅ Valid profile generated:\n")
        print(profile.json(indent=2))
    except Exception as e:
        print("❌ Validation error:", e)
        print("\nRaw Output:\n", raw_output)

if __name__ == "__main__":
    main()
