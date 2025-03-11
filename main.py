import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key from .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

# Streamlit UI
st.set_page_config(page_title="AI Study Assistant", layout="wide")
st.title("🎓 AI-Powered Study Assistant")

user_input = st.text_area("Ask me anything (e.g., Explain Neural Networks, Summarize this article...)", height=150)

if st.button("Generate Response"):
    if user_input:
        with st.spinner("Thinking..."):
            try:
                model = genai.GenerativeModel("gemini-2.0-flash")
                response = model.generate_content(user_input)
                st.subheader("📖 AI Response")
                st.write(response.text)
            except Exception as e:
                st.error(f"⚠️ Error: {e}")
    else:
        st.warning("Please enter a question or text.")
