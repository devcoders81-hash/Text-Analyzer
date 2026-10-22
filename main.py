# from src.graph import analyzer_graph
# from src.state import TextAnalyzerState


# def main() -> None:
#     print("=" * 55)
#     print("                 LLM TEXT ANALYZER")
#     print("=" * 55)

#     print(
#         "\nPaste your paragraph below. "
#         "Enter END on a new line to finish:"
#     )

#     lines = []

#     while True:
#         try:
#             line = input()
#         except EOFError:
#             break

#         if line.strip().upper() == "END":
#             break

#         lines.append(line)

#     text = "\n".join(lines).strip()

#     if not text:
#         print("Error: Text cannot be empty.")
#         return

#     # Initialize the shared graph state.
#     initial_state: TextAnalyzerState = {
#         "text": text,
#         "summary": "",
#         "sentiment": "",
#         "topic": "",
#         "keywords": [],
#     }

#     try:
#         result = analyzer_graph.invoke(initial_state)

#     except Exception as exc:
#         print(f"\nAnalysis failed: {exc}")
#         return

#     print("\n" + "=" * 55)
#     print("                  ANALYSIS REPORT")
#     print("=" * 55)

#     print("\n1. SUMMARY")
#     print(result["summary"])

#     print("\n2. SENTIMENT")
#     print(result["sentiment"])

#     print("\n3. TOPIC CLASSIFICATION")
#     print(result["topic"])

#     print("\n4. KEYWORDS")

#     for index, keyword in enumerate(
#         result["keywords"], start=1
#     ):
#         print(f"{index}. {keyword}")

#     print("\n" + "=" * 55)


# if __name__ == "__main__":
#     main()

import streamlit as st

from src.graph import analyzer_graph
from src.state import TextAnalyzerState


# --------------------------------------------------
# 1. Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="LLM Text Analyzer",
    page_icon="🧠",
    layout="wide",
)

st.title("🧠 LLM Text Analyzer")

st.write(
    "Analyze long paragraphs using an LLM-powered "
    "LangGraph workflow."
)

st.divider()


# --------------------------------------------------
# 2. User Input
# --------------------------------------------------

with st.form("text_analyzer_form"):

    text = st.text_area(
        "Enter your paragraph",
        placeholder=(
            "Example: I bought a laptop from an online "
            "store, but delivery was delayed..."
        ),
        height=220,
    )

    submitted = st.form_submit_button(
        "Analyze Text",
        type="primary",
        use_container_width=True,
    )


# --------------------------------------------------
# 3. Execute LangGraph
# --------------------------------------------------

if submitted:

    if not text.strip():
        st.warning("Please enter a paragraph first.")

    else:
        # Initialize shared graph state.
        initial_state: TextAnalyzerState = {
            "text": text.strip(),
            "summary": "",
            "sentiment": "",
            "topic": "",
            "keywords": [],
        }

        try:
            # Show progress while all four nodes execute.
            with st.spinner(
                "Analyzing your text. Please wait..."
            ):
                result = analyzer_graph.invoke(initial_state)

            st.success("Analysis completed successfully!")

            # ------------------------------------------
            # 4. Display Summary
            # ------------------------------------------

            st.header("📄 Analysis Report")

            st.subheader("1. Summary")

            st.write(result["summary"])

            st.divider()

            # ------------------------------------------
            # 5. Display Sentiment and Topic
            # ------------------------------------------

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("2. Sentiment Analysis")

                st.metric(
                    label="Overall Sentiment",
                    value=result["sentiment"],
                )

            with col2:
                st.subheader("3. Topic Classification")

                st.write(result["topic"])

            st.divider()

            # ------------------------------------------
            # 6. Display Keywords
            # ------------------------------------------

            st.subheader("4. Keyword Extraction")

            keywords = result["keywords"]

            if keywords:
                for index, keyword in enumerate(
                    keywords,
                    start=1,
                ):
                    st.write(f"{index}. {keyword}")
            else:
                st.info("No keywords were extracted.")

            # ------------------------------------------
            # 7. Display Original Text
            # ------------------------------------------

            with st.expander("View Original Text"):
                st.write(text.strip())

        except Exception as exc:
            st.error(f"Analysis failed: {exc}")