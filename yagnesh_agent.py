import streamlit as st
from openai import OpenAI
import os

# Page title
st.set_page_config(page_title="Yagnesh Agent", layout="centered")
st.title("🤖 Yagnesh Agent")

# Get OpenAI API key (You can set it as environment variable or use Streamlit secrets)
api_key = "<replace your Api key>"

if not api_key:
    st.error("Please set your OpenAI API key in Streamlit secrets or as an environment variable.")
    st.stop()

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Input from user
user_input = st.text_input("Ask anything:")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are Yagnesh Agent, a helpful assistant."}]

# Process user input
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get response from OpenAI
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages
        )

    # Extract assistant message
    assistant_reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})

# Display chat history
for msg in st.session_state.messages[1:]:
    is_user = msg["role"] == "user"
    st.markdown(f"**{'You' if is_user else 'Yagnesh Agent'}:** {msg['content']}")
