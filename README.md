# 🤖 AI Chatbot (Gemini + Streamlit)

A simple and interactive AI chatbot built using Streamlit and Google Gemini API.  
This project demonstrates how to build a conversational AI interface with short-term memory using session state.

---

## 🚀 Features

- 💬 Real-time chat interface using Streamlit
- 🧠 Short-term memory using st.session_state
- ⚡ Powered by Google Gemini LLM (gemini-3.5-flash)
- 🎯 Maintains conversation context during session
- 🖥️ Clean and minimal UI

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Generative AI (Gemini)
- python-dotenv

---

## 📂 Project Structure

AI_Chatbot/
│── app.py
│── .env
│── requirements.txt
│── README.md

---

## ⚙️ Installation & Setup

### 1. Clone the repository
git clone https://github.com/ikbalhussa1n/AI_Chatbot.git
cd AI_Chatbot

### 2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

### 3. Install dependencies
pip install -r requirements.txt

### 4. Add API Key
Create a .env file:
api_key=YOUR_GOOGLE_GEMINI_API_KEY

### 5. Run the app
streamlit run app.py

---

## 🧠 How It Works

User message → stored in session_state  
Conversation history → sent to Gemini  
Gemini responds using full context  
Response → displayed + stored again  

This enables short-term memory chat behavior.

---

## 🔥 Example

User: I have 7 apples  
Bot: Nice!

User: How many apples do I have?  
Bot: You have 7 apples.

---

## 🚀 Future Improvements

- Long-term memory (DB / vector store)
- Voice chat
- Deployment on Streamlit Cloud
- User authentication

---

## 👨‍💻 Author
GitHub: https://github.com/ikbalhussa1n
