# --- FILE: evaluation.py ---
def evaluate_quality(profile, enrichment_keywords):
    overview_text = profile.overview.lower()
    matched_keywords = [kw for kw in enrichment_keywords if kw.lower() in overview_text]
    coverage = len(matched_keywords) / len(enrichment_keywords) if enrichment_keywords else 0
    return {"matched_keywords": matched_keywords, "coverage": coverage}