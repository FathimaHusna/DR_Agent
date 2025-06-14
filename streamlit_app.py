import streamlit as st
import json
import re
from agent import run_profile_agent
from schema import UpworkProfile

def extract_json(text):
    match = re.search(r"\{.*\}", text, re.DOTALL)
    return match.group(0) if match else None

st.title("🔍 Deep Research Agent — Upwork Profile Generator")

role = st.text_input("Role", "Python Developer")
experience = st.text_input("Experience", "2 years")
skills_input = st.text_input("Skills (comma-separated)", "Selenium, Web Scraping, Automation")
rate = st.text_input("Hourly Rate", "$15/hr")

if st.button("Generate Profile"):
    skills = [s.strip() for s in skills_input.split(",")]
    raw_output = run_profile_agent(role, experience, skills, rate)

    st.subheader("🔧 Raw Output")
    st.code(raw_output)

    cleaned_output = extract_json(raw_output)

    if not cleaned_output:
        st.error("❌ No valid JSON found in the output.")
        st.stop()

    try:
        parsed = json.loads(cleaned_output)

        # Auto-fix hourly_rate if needed
        if isinstance(parsed.get("hourly_rate"), (int, float)):
            parsed["hourly_rate"] = f"${parsed['hourly_rate']}/hr"

        profile = UpworkProfile(**parsed)

        st.success("✅ Valid Upwork profile generated!")
        st.json(profile.model_dump())

    except Exception as e:
        st.error(f"❌ Validation Failed!\n{e}")
        st.code(cleaned_output)