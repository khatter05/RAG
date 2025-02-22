import streamlit as st
from app.main import ask_question

# Streamlit UI
st.title("AI Chat with DeepSeek & ChromaDB")
st.write("Ask a question based on stored knowledge!")

question = st.text_input("Enter your question:")
if st.button("Ask"):
    if question.strip():
        with st.spinner("Thinking..."):
            answer = ask_question(question)
            st.success(answer)
    else:
        st.warning("Please enter a question.")
