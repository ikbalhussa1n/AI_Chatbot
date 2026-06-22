from google import genai
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

api_key = os.getenv("api_key")
client = genai.Client(api_key=api_key)

st.title("My Gemini Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])



prompt = st.chat_input("Type your message here...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = client.models.generate_content(
        model='gemini-3.5-flash',
        contents=list(map(lambda message: message['role'] + ": " + message['content'], st.session_state.messages)),
    )

    st.session_state.messages.append(
        {"role": "assistant", 
        "content": response.text}
        )
    with st.chat_message("assistant"):
        st.markdown(response.text)