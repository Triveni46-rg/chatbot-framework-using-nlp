import nltk
import random
import re
import streamlit as st
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download required NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Expanded chatbot responses
responses = {
    r"hello|hi|hey": ["Hi there!", "Hello!", "Hey! How can I assist you?"],
    r"how are you": ["I'm just a bot, but I'm doing great!", "I'm fine, thank you!", "I'm doing well, how about you?"],
    r"what is your name|who are you": ["I'm your friendly chatbot!", "You can call me ChatBot!", "I'm just a virtual assistant."],
    r"what can you do": ["I can chat with you, answer questions, and make your day better!", "I can respond to simple queries. Try asking me something!"],
    r"your favorite (food|drink)": ["I don’t eat, but I hear pizza is great!", "I survive on data and electricity!"],
    r"what is your purpose": ["I'm here to chat and assist you with anything I can!", "To talk to you and make your life easier."],
    r"tell me a joke": ["Why did the computer go to therapy? It had too many bugs!", "Why don’t robots have brothers? Because they only have trans-sisters!"],
    r"(.*)weather(.*)": ["I can't check the weather, but I hope it's nice where you are!", "I hope it's sunny and bright today!"],
    r"(.*)your age(.*)": ["I exist outside of time, but I was created recently!", "I don’t age, I just keep learning!"],
    r"(.*)like(.*)": ["I like talking to you!", "I enjoy helping people with their questions."],
    r"(.*)love(.*)": ["Love is a wonderful thing!", "Love makes the world go round!"],
    r"(.*)sad(.*)|depressed|unhappy": ["I'm here for you! Want to talk about it?", "Sometimes talking to someone helps. I'm here!"],
    r"(.*)hobby(.*)": ["I enjoy learning new things and chatting with you!", "Helping you is my favorite hobby!"],
    r"(.*)bye(.*)": ["Goodbye!", "See you later!", "Take care!"]
}

# Function to get chatbot response
def get_response(user_input):
    user_input = user_input.lower()

    for pattern, replies in responses.items():
        if re.search(pattern, user_input):  # Check if user input matches any pattern
            return random.choice(replies)
    
    return random.choice(["I'm not sure I understand.", "Can you rephrase that?", "That's interesting! Tell me more."])

# Streamlit UI
st.title("💬 Simple Chatbot")
st.write("🤖 Type your message below and chat with the bot!")

# Maintain chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Use st.chat_input for better interaction
user_input = st.chat_input("Type your message...")

if user_input:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)
    
    # Get chatbot response
    bot_response = get_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    st.chat_message("assistant").write(bot_response)
