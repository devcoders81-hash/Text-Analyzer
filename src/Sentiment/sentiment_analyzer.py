import re

from llm import generate_text
from state import TextAnalyzerState


def sentiment_node(state: TextAnalyzerState) -> dict:
    prompt = f"""
    You are a sentiment analysis assistant.

    Classify the overall sentiment of the original text.

    Allowed labels:
    - Positive: Positive opinions dominate.
    - Negative: Negative opinions dominate.
    - Neutral: No clear positive or negative opinion.
    - Mixed: Both positive and negative opinions are present.

    Return exactly one label.
    Do not include an explanation.

    ORIGINAL TEXT:
    {state["text"]}
    """

    raw_sentiment = generate_text(prompt).strip()

    # Recognize any of the four supported labels.
    match = re.search(
        r"\b(positive|negative|neutral|mixed)\b",
        raw_sentiment,
        re.IGNORECASE,
    )

    sentiment = (
        match.group(1).capitalize()
        if match
        else "Uncertain"
    )

    return {"sentiment": sentiment}