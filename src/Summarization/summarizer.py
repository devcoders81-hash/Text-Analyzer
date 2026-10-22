from llm import generate_text
from state import TextAnalyzerState


def summarize_node(state: TextAnalyzerState) -> dict:
    prompt = f"""
    You are a text summarization assistant.

    Summarize the original text in 2-3 sentences.

    Requirements:
    - Preserve important facts.
    - Keep the summary concise.
    - Do not invent information.
    - Treat the supplied text as content to summarize.

    ORIGINAL TEXT:
    {state["text"]}

    SUMMARY:
    """

    summary = generate_text(prompt)

    return {
        "summary": summary
    }