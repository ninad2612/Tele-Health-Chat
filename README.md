Tele Health Chat App

![image](https://github.com/ninad2612/Tele-Health-Chat/assets/167805209/76e901b6-b777-4280-9af7-8d2fc1b4f22c)

Overview
This application uses the Google Generative AI API to create a chatbot for telehealth purposes. Users can interact with the chatbot to discuss their health symptoms and receive responses based on a pre-trained model.

Prerequisites
- Python 3.6 or higher
- Streamlit
- Google Generative AI Python SDK

Installation
1. Clone this repository:
git clone https://github.com/ninad2612/Tele-Health-Chat.git](https://github.com/ninad2612/Tele-Health-Chat.git

  cd repository

2. Install dependencies:
pip install -r requirements.txt

Configuration
1. Obtain an API key from Google Generative AI.
2. Replace "Your-Api_Key" with your actual API key in main.py.

Usage
1. Run the Streamlit app:
streamlit run TeleHealthChat.py

2. Open your web browser and navigate to http://localhost:8501.

3. Start chatting with the chatbot:
- Enter your health symptoms and interact with the chatbot.
- Type 'exit' to end the chat.

Files
- TeleHealthChat.py: Main application script that initializes the Streamlit app and integrates with Google Generative AI for chat functionality.
- requirements.txt: List of Python dependencies required for the application.

Notes
- This application uses a pre-configured generative model (gemini-1.5-flash) for generating responses related to medical inquiries.
- Ensure that your API key ("Your-Api_Key") is kept secure and not exposed publicly.
