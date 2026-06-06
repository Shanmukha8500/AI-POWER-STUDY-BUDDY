import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API Key
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")


if not API_KEY:
    st.error("API Key not found in .env file")
    st.stop()

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(
    page_title="AI Study Buddy",
    page_icon="📚",
    layout="wide"
)

st.title("📚 AI-Powered Study Buddy")
st.write("Explain Topics | Summarize Notes | Generate Quizzes | Create Flashcards")

feature = st.sidebar.selectbox(
    "Choose Feature",
    [
        "Topic Explainer",
        "Notes Summarizer",
        "Quiz Generator",
        "Flashcard Generator"
    ]
)

# -------------------------------
# Topic Explainer
# -------------------------------
if feature == "Topic Explainer":

    st.header("🧠 Explain Any Topic")

    topic = st.text_input("Enter Topic")

    if st.button("Explain"):

        prompt = f"""
        Explain the topic '{topic}'
        in very simple language.
        Give examples.
        Use bullet points.
        """

        with st.spinner("Generating Explanation..."):
            response = model.generate_content(prompt)

        st.success("Done!")
        st.write(response.text)

# -------------------------------
# Notes Summarizer
# -------------------------------
elif feature == "Notes Summarizer":

    st.header("📝 Summarize Notes")

    notes = st.text_area(
        "Paste Notes",
        height=300
    )

    if st.button("Summarize"):

        prompt = f"""
        Summarize the following notes.

        Notes:
        {notes}

        Give:
        1. Short Summary
        2. Key Points
        3. Important Terms
        """

        with st.spinner("Summarizing..."):
            response = model.generate_content(prompt)

        st.success("Summary Ready")
        st.write(response.text)

# -------------------------------
# Quiz Generator
# -------------------------------
elif feature == "Quiz Generator":

    st.header("❓ Generate Quiz")

    topic = st.text_input("Quiz Topic")

    difficulty = st.selectbox(
        "Difficulty",
        ["Easy", "Medium", "Hard"]
    )

    num_questions = st.slider(
        "Number of Questions",
        5,
        20,
        10
    )

    if st.button("Generate Quiz"):

        prompt = f"""
        Create {num_questions} MCQ questions.

        Topic: {topic}
        Difficulty: {difficulty}

        Include:
        - Question
        - 4 Options
        - Correct Answer
        """

        with st.spinner("Generating Quiz..."):
            response = model.generate_content(prompt)

        st.success("Quiz Generated")
        st.write(response.text)

# -------------------------------
# Flashcards
# -------------------------------
elif feature == "Flashcard Generator":

    st.header("🗂 Generate Flashcards")

    content = st.text_area(
        "Enter Notes or Topic",
        height=250
    )

    if st.button("Generate Flashcards"):

        prompt = f"""
        Create flashcards from:

        {content}

        Format:

        Q:
        A:

        Generate at least 10 flashcards.
        """

        with st.spinner("Creating Flashcards..."):
            response = model.generate_content(prompt)

        st.success("Flashcards Ready")
        st.write(response.text)

# Footer
st.markdown("---")
st.markdown(
    "Developed with Python, Streamlit and Google Gemini AI"
)