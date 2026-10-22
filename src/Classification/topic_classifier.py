from llm import generate_text
from state import TextAnalyzerState


def topic_node(state: TextAnalyzerState) -> dict:
    prompt = f"""
    You are a text topic classification assistant.

    Identify the main topic of the original text.
    You may also identify one or two relevant subtopics.

    Requirements:
    - Be concise.
    - Do not summarize the entire paragraph.
    - Do not invent details.

    Return your answer in this format:

    Main topic: <topic>
    Subtopics: <subtopics>

    ORIGINAL TEXT:
    {state["text"]}
    """

    topic = generate_text(prompt)

    return {
        "topic": topic
    }