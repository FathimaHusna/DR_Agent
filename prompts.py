def build_prompt(role, experience, skills, rate, tone):
    return f"""
You are an expert Upwork freelancer.

Create a professional Upwork profile for a {role} with {experience} of experience.
Mention the following core skills: {', '.join(skills)}.
The hourly rate must be included as a string like "{rate}" with a "$" symbol and "/hr".
Write the profile in a {tone.lower()} tone.

Return ONLY a JSON object with these fields:
- title (string)
- overview (string)
- skills (list of strings)
- hourly_rate (string formatted like "$15/hr")
- profile_tips (list of 3–5 strings)

Respond with valid JSON only. No markdown, no explanations.
"""
