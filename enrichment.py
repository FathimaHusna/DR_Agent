def generate_enrichment_context(role, skills, content):
    extracted_keywords = set()
    for text in content:
        for word in text.split():
            if any(skill.lower() in word.lower() for skill in skills):
                extracted_keywords.add(word.strip(".,:;-"))
    enriched_lines = [f"- Emphasize {kw}" for kw in sorted(extracted_keywords)]
    return "\n".join(enriched_lines)