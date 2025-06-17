from scraper import get_cached_or_fetch_profiles
from enrichment import generate_enrichment_context
from prompts import build_prompt
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

def run_profile_agent(role, experience, skills, rate, tone):
    urls, content = get_cached_or_fetch_profiles(role)
    enrichment = generate_enrichment_context(role, skills, content)
    prompt = build_prompt({
        "role": role,
        "experience": experience,
        "skills": skills,
        "rate": rate,
        "tone": tone
    }, enrichment)
    response = model.generate_content(prompt)
    return response.text.strip()
