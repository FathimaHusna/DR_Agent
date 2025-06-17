def build_prompt(user_input, enrichment):
    return f'''
Act as a professional Upwork profile writer.
Generate a JSON profile using the following input:

Role: {user_input['role']}
Skills: {', '.join(user_input['skills'])}
Experience: {user_input['experience']}
Hourly Rate: {user_input['rate']}
Tone: {user_input['tone']}

Enrichment context:
{enrichment}

Return ONLY a valid JSON object with:
- title (string)
- overview (string)
- skills (list of strings)
- hourly_rate (string)
- profile_tips (list of 3–5 strings)

No markdown. No explanations.
'''