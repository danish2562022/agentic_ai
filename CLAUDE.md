# agentic_ai — Project Instructions

## Project Overview
An AI/LLM agent project using multiple model providers and LangChain for orchestration.

## Tech Stack
- **Language:** Python 3.10+
- **LLM Providers:** OpenAI, Groq, Hugging Face
- **Orchestration:** LangChain / LangSmith
- **Environment:** `.env` file for secrets (never commit)

## Project Structure
```
agent_ai/
├── main.py          # Entry point
├── .env             # API keys (gitignored)
├── .gitignore
└── CLAUDE.md
```

## Entry Point
```bash
python main.py
```

## Environment Setup
```bash
# Copy env template and fill in keys
cp .env.example .env

# Install dependencies
pip install -r requirements.txt
```

## Environment Variables (in .env)
| Variable | Purpose |
|---|---|
| OPENAI_API_KEY | OpenAI API access |
| LANGCHAIN_API_KEY | LangSmith tracing |
| LANGCHAIN_PROJECT | LangSmith project name |
| HF_TOKEN | Hugging Face model access |
| GROQ_API_KEY | Groq inference API |

## Important Rules
- Never commit `.env`
- Load env vars with `python-dotenv`
- Use LangSmith for tracing LangChain runs

## Remote
- GitHub: https://github.com/danish2562022/agentic_ai
- Branch: `main`
