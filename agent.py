import os
import google.generativeai as genai
from dotenv import load_dotenv
from prompts import build_prompt


load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

def run_profile_agent(role, experience, skills, rate, tone):
    prompt = build_prompt(role, experience, skills, rate, tone)
    response = model.generate_content(prompt)
    return response.text.strip()
