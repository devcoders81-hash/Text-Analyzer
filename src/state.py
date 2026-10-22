from typing import TypedDict


class TextAnalyzerState(TypedDict):
    text: str
    summary: str
    sentiment: str
    topic: str
    keywords: list[str]