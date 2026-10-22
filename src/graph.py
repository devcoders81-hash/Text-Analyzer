from langgraph.graph import StateGraph, START, END

from state import TextAnalyzerState
from src.Summarization.summarizer import summarize_node
from src.Sentiment.sentiment_analyzer import sentiment_node
from src.Classification.topic_classifier import topic_node
from src.Extractor.keyword_extractor import keywords_node
builder = StateGraph(TextAnalyzerState)

builder.add_node("summarize", summarize_node)
builder.add_node("sentiment", sentiment_node)
builder.add_node("topic", topic_node)
builder.add_node("keywords", keywords_node)

builder.add_edge(START, "summarize")
builder.add_edge("summarize", "sentiment")
builder.add_edge("sentiment", "topic")
builder.add_edge("topic","keywords")
builder.add_edge("keywords",END)


analyzer_graph = builder.compile()