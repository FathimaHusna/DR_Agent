import streamlit as st
import json
import re
from agent import run_profile_agent
from schema import UpworkProfile

def extract_json(text):
    """Extracts the first valid JSON block from the model output."""
    match = re.search(r"\{.*\}", text, re.DOTALL)
    return match.group(0) if match else None

# Page Title
st.set_page_config(page_title="Upwork Profile Generator", layout="centered")
st.title("🔍 Deep Research Agent — Upwork Profile Generator")

# Input Fields
role = st.text_input("Role", "Python Developer")
experience = st.text_input("Experience", "2 years")
skills_input = st.text_input("Skills (comma-separated)", "Selenium, Web Scraping, Automation")
rate = st.text_input("Hourly Rate", "$15/hr")
tone = st.selectbox("Tone", ["Professional", "Friendly", "Casual", "Concise"], index=0)

# When Button Clicked
if st.button("✨ Generate My Upwork Profile"):
    skills = [s.strip() for s in skills_input.split(",") if s.strip()]
    raw_output = run_profile_agent(role, experience, skills, rate, tone)

    st.subheader("🧠 LLM Output")
    st.code(raw_output, language="json")

    cleaned_output = extract_json(raw_output)

    if not cleaned_output:
        st.error("❌ No valid JSON found in the response. Please try different inputs.")
        st.stop()

    try:
        parsed = json.loads(cleaned_output)

        # Auto-fix hourly_rate formatting if needed
        if isinstance(parsed.get("hourly_rate"), (int, float)):
            parsed["hourly_rate"] = f"${parsed['hourly_rate']}/hr"

        # Validate with schema
        profile = UpworkProfile(**parsed)

        st.success("✅ Success! Here's your optimized profile:")
        st.json(profile.model_dump())

        # Downloadable JSON
        st.download_button("⬇️ Download JSON", json.dumps(profile.model_dump(), indent=2), file_name="upwork_profile.json")

    except Exception as e:
        st.error(f"❌ Validation Error: {e}")
        st.text_area("🔍 Raw JSON for Debugging", value=cleaned_output, height=200)
