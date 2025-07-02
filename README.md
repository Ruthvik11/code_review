🧠 LLM-Powered Code Review Bot
An intelligent and sarcastic Python code review assistant powered by GPT-3.5, LangChain, ChromaDB, and served through FastAPI + Streamlit. This tool not only identifies issues in your code but also delivers witty roasts to keep you entertained! 🤖🔥
🚀 Live 
 👉 [Try the Streamlit App](https://codereview-yo4psvunp2xfpczhnjqcrs.streamlit.app/)
Streamlit Demo
📸 Preview

🛠 Features

GPT-3.5 powered sarcastic code reviews
Retrieval-Augmented Generation (RAG) using ChromaDB
Source-aware feedback with real-world examples
FastAPI backend and Streamlit frontend
Swagger documentation for API testing
Open-source Python code indexing from TheAlgorithms repo

🧱 Tech Stack



Layer
Tools



LLM
OpenAI GPT-3.5


RAG
LangChain + ChromaDB


Embeddings
OpenAI Embeddings


Backend
FastAPI + Pydantic


Frontend
Streamlit


Loader
LangChain TextLoader


Deployment
(Upcoming: Streamlit Cloud)


🧪 How It Works

TheAlgorithms/Python repo is embedded into ChromaDB.
Users paste Python code into the UI.
Relevant examples are retrieved via semantic search (RAG).
GPT-3.5 processes the user’s code, similar code context, and a sarcastic prompt.
A witty, actionable review is returned.

📂 Folder Structure
```bash
code_review_bot/
├── app/              # Streamlit frontend
├── backend/          # FastAPI backend
├── data/             # ChromaDB storage
├── docs/             # Swagger docs
├── scripts/          # Data loading scripts
├── requirements.txt  # Project dependencies
└── README.md         # This file
```
🚀 Getting Started
Prerequisites

Python 3.9+
Git
An OpenAI API key

Installation

Clone the repository:
git clone https://github.com/your-username/code_review_bot.git
cd code_review_bot


Install dependencies:
pip install -r requirements.txt


Set up your OpenAI API key:
export OPENAI_API_KEY='your-api-key-here'


Run the backend:
cd backend
uvicorn main:app --reload


Run the frontend:
cd app
streamlit run app.py



🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. For major changes, open an issue first to discuss.

🙏 Acknowledgments

Inspired by TheAlgorithms/Python repo
Built with love using open-source tools
