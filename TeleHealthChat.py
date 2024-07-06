import os
import google.generativeai as genai
import streamlit as st

# Configure the API key
genai.configure(api_key="Your-Api_Key")

# Create the model generation_config
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="You are a Medical Llm that will have conversation with patients in question and answer format. And after 3-4 Questions finally give some remedy \n",
)

def start_chat():
    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": ["hii\n"],
            },
            {
                "role": "model",
                "parts": ["Hi! How can I help you today?\n"],
            },
        ]
    )
    return chat_session

# Streamlit app
def app():
    st.title("Tele Health")
    st.subheader("Welcome to the Tele health Chat! Tell me about your health symptoms.")
    st.write("Type 'exit' to end the chat.")

    chat_session = start_chat()
    chat_history = st.empty()

    user_input = st.text_input("You: ", key="input")
    if user_input.lower() in ["exit", "quit"]:
        st.write("Goodbye!")
        st.stop()

    if user_input:
        try:
            response = chat_session.send_message(user_input)
            chat_history.write(f"You: {user_input}")
            chat_history.write(f"Chatbot: {response.text}")
        except Exception as e:
            st.write(f"Sorry, I couldn't generate a response. Please try again. Error: {e}")

if __name__ == "__main__":
    app()
