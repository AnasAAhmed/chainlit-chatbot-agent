# 💬 Chainlit-Based AI Translator Agent with Streaming Output

An interactive AI translation chatbot powered by Google Gemini and built using Chainlit. The agent translates human language input into any specified language with real-time streaming output.

---

## 🧠 Project Purpose

This chatbot was created as part of the **Governor House AI & Cloud First Initiative** and **Panaverse DAO** curriculum. The project demonstrates how to build conversational agents using LLMs, Chainlit, and streaming interfaces.

---

## 🚀 Features

- 🌍 Translate text to any human language
- ⚡ Powered by Google Gemini (OpenAI-compatible API)
- 🧠 AI agent with dynamic instructions
- 💬 Real-time streaming responses
- 🧱 Modular architecture using `Runner`, `Agent`, `RunConfig`
- 🎨 Built using Chainlit for a chat UI experience

---

## 🛠️ Technologies Used

- Python 3.9+
- [Chainlit](https://www.chainlit.io/)
- Google Gemini via OpenAI-compatible endpoint
- `python-dotenv`
- Agents library (`Runner`, `Agent`, etc.)

---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/chainlit-ai-translator.git
cd chainlit-ai-translator
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a .env file
```bash
GEMINI_API_KEY=your_google_gemini_api_key
```