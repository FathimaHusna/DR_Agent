import streamlit as st
from agent import run_profile_agent
from validation import validate_inputs
import json, re
from schema import UpworkProfile
from evaluation import evaluate_quality

def extract_json(text):
    match = re.search(r"\{.*\}", text, re.DOTALL)
    return match.group(0) if match else None

st.title("🔧 AI Upwork Profile Generator")

role = st.text_input("Role", "Python Developer")
experience = st.text_input("Experience", "2 years")
skills = st.text_input("Skills (comma separated)", "Django, Flask, REST API")
rate = st.text_input("Hourly Rate", "$20/hr")
tone = st.selectbox("Tone", ["Professional", "Friendly", "Direct", "Inspiring"])

if st.button("Generate Profile"):
    skills_list = [s.strip() for s in skills.split(",") if s.strip()]
    errors = validate_inputs(role, experience, skills_list, rate, tone)

    if errors:
        for err in errors:
            st.error(f"⚠️ {err}")
    else:
        with st.spinner("Generating..."):
            output = run_profile_agent(role, experience, skills_list, rate, tone)
            json_text = extract_json(output)

            if json_text:
                parsed = json.loads(json_text)
                st.subheader("✅ Generated Profile")
                st.json(parsed)

                profile = UpworkProfile(**parsed)
                evaluation = evaluate_quality(profile, skills_list)

                st.subheader("📊 Keyword Evaluation")
                st.write(f"Matched Keywords: {evaluation['matched_keywords']}")
                st.write(f"Coverage: {evaluation['coverage'] * 100:.2f}%")
            else:
                st.error("❌ Failed to extract valid profile output.")
