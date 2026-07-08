import streamlit as st

st.title("EduGenie - AI Educational Assistant")

option = st.selectbox(
    "Choose a feature",
    [
        "Question Answering",
        "Concept Explanation",
        "Quiz Generation",
        "Text Summarization",
        "Learning Recommendations"
    ]
)

text = st.text_area("Enter your topic or question")

if st.button("Submit"):
    if option == "Question Answering":
        st.write("Answer:")
        st.write("Python is a programming language.")

    elif option == "Concept Explanation":
        st.write("Explanation:")
        st.write(f"{text} is an important concept that can be learned step by step.")

    elif option == "Quiz Generation":
        st.write("1. What is " + text + "?")
        st.write("2. Explain the uses of " + text)

    elif option == "Text Summarization":
        st.write("Summary:")
        st.write(text[:100])

    elif option == "Learning Recommendations":
        st.write("Recommendation:")
        st.write("1. Learn the basics")
        st.write("2. Practice examples")
        st.write("3. Build small projects")
        st.write("4. Learn advanced topics")