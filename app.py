import os
from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
from langchain.schema import SystemMessage, HumanMessage
from my_prompt import make_prompt   

# Load environment variables
load_dotenv()

# Streamlit App
st.set_page_config(page_title="LLM Topic Generator", page_icon="🤖", layout="centered")

st.title("🤖 Topic Explanation Generator")
st.write("Enter a topic and get 3 concise, structured points.")

# User input
topic = st.text_input("Enter your topic:")

if st.button("Generate Response"):
    if not topic.strip():
        st.warning("⚠️ Please enter a topic first.")
    else:
        with st.spinner("Generating your response..."):
            # Initialize Groq LLM
            llm = ChatGroq(
                groq_api_key=os.getenv("GROQ_API"),
                model="llama-3.1-8b-instant"
            )

            # Build prompt
            prompt = make_prompt(topic)
            messages = [
                SystemMessage(content="You are an assistant that must always follow the given format and rules."),
                HumanMessage(content=prompt)
            ]

            # Get response
            response = llm.invoke(messages)

            # Display result
            st.success("✅ Response generated successfully!")
            st.text_area("Output:", value=response.content, height=200)
