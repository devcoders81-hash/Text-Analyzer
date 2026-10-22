import json

from llm import generate_text
from state import TextAnalyzerState


def keywords_node(state: TextAnalyzerState) -> dict:
    prompt = f"""
    You are a keyword extraction assistant.

    Extract 5-10 important keywords or key phrases
    from the original text.

    Rules:
    - Prefer meaningful phrases over generic words.
    - Use only concepts supported by the original text.
    - Return ONLY a valid JSON array of strings.
    - Do not add explanations.

    Example:
    ["delayed delivery", "customer support", "refund"]

    ORIGINAL TEXT:
    {state["text"]}
    """

    raw_output = generate_text(prompt)

    # Remove optional Markdown formatting.
    cleaned = raw_output.strip()

    if cleaned.startswith("```"):
        cleaned = cleaned.split("\n", 1)[-1]
        cleaned = cleaned.rsplit("```", 1)[0].strip()

    # Extract the JSON array if the model adds extra text.
    start = cleaned.find("[")
    end = cleaned.rfind("]")

    if start != -1 and end > start:
        cleaned = cleaned[start:end + 1]

    try:
        keywords = json.loads(cleaned)

        if not isinstance(keywords, list):
            raise ValueError("Expected a JSON array.")

    except (json.JSONDecodeError, ValueError):
        # Basic fallback for comma-separated responses.
        keywords = cleaned.split(",")

    keywords = [
        str(keyword).strip().strip("\"'")
        for keyword in keywords
        if str(keyword).strip()
    ]

    return {
        "keywords": keywords[:10]
    }