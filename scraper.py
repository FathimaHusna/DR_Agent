import os, json
from duckduckgo_search import DDGS
from utils import load_cache, save_cache

def get_cached_or_fetch_profiles(role):
    cache = load_cache()
    if role in cache:
        return cache[role]["urls"], cache[role]["content"]

    query = f'site:upwork.com/freelancers "{role}"'
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=10)
        urls = [r["href"] for r in results if "upwork.com/freelancers/" in r["href"]]

    # Simulated scraping output for keyword extraction
    content = [
        "Experienced with Selenium, Automation, and Web Scraping. Fast-loading websites with responsive design.",
        "Modern UI specialist using Django, Flask, and REST APIs."
    ]

    cache[role] = {"urls": urls, "content": content}
    save_cache(cache)
    return urls, content