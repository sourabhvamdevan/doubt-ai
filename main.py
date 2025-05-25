

import streamlit as st
from allagents.tutor_agent import TutorAgent
from utilities.memory import MemoryBuffer

# Initialize session state
if "memory" not in st.session_state:
    st.session_state.memory = MemoryBuffer()
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# App layout
st.set_page_config(page_title="AI Tutor", page_icon="🧠")

# Sidebar
with st.sidebar:
    st.title("⚙️ AI Tutor Settings")
    temperature = st.slider("Model Creativity", 0.1, 1.0, 0.7)
    if st.button("Clear Conversation"):
        st.session_state.memory.clear()
        st.session_state.chat_history = []

# Main chat interface
st.title("🧠 AI Tutor - Your Personal Learning Assistant")

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask your question about Math, Physics, or Chemistry..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get AI response
    with st.spinner("Thinking..."):
        tutor = TutorAgent(temperature=temperature)
        response = tutor.ask(prompt, st.session_state.memory)
    
    with st.chat_message("assistant"):
        st.markdown(response)
    
    st.session_state.chat_history.append({"role": "assistant", "content": response})