import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise RuntimeError(
        "GROQ_API_KEY is missing from the .env file."
    )

llm = ChatGroq(
    model=os.getenv("GROQ_MODEL", "openai/gpt-oss-20b"),
    api_key=api_key,
    temperature=0,
)


def generate_text(prompt: str) -> str:
    """Send a prompt to the LLM and return its response."""
    response = llm.invoke(prompt)

    if isinstance(response.content, str):
        return response.content.strip()

    return str(response.content).strip()