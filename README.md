# 🧠 Deep Research Agent (Phase 1) – Upwork Profile Generator

This is the Phase 1 implementation of a Deep Research Agent project, focused on generating optimized Upwork profiles using LLMs like Google Gemini.

---

## 📁 Project Structure

```
DR_AGENT/
├── main.py              # Command-line runner
├── agent.py             # Core logic to query Gemini
├── prompts.py           # Prompt template for Gemini
├── schema.py            # Pydantic model for profile validation
├── test_main.py         # Pytest validation script
├── streamlit_app.py     # Streamlit UI to run in browser
├── requirements.txt     # Dependencies
├── .env                 # Store API keys and config
```
(exp.ipynb) #Notebook
---

## 🚀 How to Run

### 1. Create and activate virtual environment
```bash
python -m venv dr_env
source dr_env/bin/activate  # On Windows: dr_env\Scripts\activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your Google Gemini API key to `.env`
```
GEMINI_API_KEY=your_api_key_here
```

### 4. Run via Streamlit
```bash
streamlit run streamlit_app.py
```

---

## 🧪 Testing

```bash
pytest test_main.py
```

---

## ✅ Output Format

Returns a validated JSON Upwork profile:
```json
{
  "title": "Experienced Python Developer | Selenium Expert",
  "overview": "...",
  "skills": [...],
  "hourly_rate": "$15/hr",
  "profile_tips": [...]
}
```

## 📸 Streamlit Output Example

![Streamlit Screenshot](.ss1.png)
![Streamlit Screenshot](.ss2.png)

---

## 📌 Notes

- Uses **Pydantic** to validate and clean model output
- Uses **Streamlit** for interactive browser UI
- Output is consumable for further use (e.g., profile auto-filling bots)

---

## 📫 Author

Built with ❤️ by Husna