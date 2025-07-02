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
├── Python/
├── app.py
├── main.py
├── logic.py
├── model.py
├── prompt.py
├── model_loader.py
├── rag_loader.py
├── rag_reviewer.py
├── run_loader.py
├── requirements.txt
├── README.md
└── .gitignore
```
## 🚀 Getting Started

### 🧰 Prerequisites
- Python 3.9+
- Git
- OpenAI API key

### ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/Ruthvik11/code_review.git
cd code_review

# (Optional) Create and activate virtual environment
python -m venv env
env\Scripts\activate        # For Windows
source env/bin/activate     # For Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Set your OpenAI API key
echo OPENAI_API_KEY=your-api-key-here > .env

# Run the backend
uvicorn main:app --reload

# Run the frontend
streamlit run app.py



🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. For major changes, open an issue first to discuss.

🙏 Acknowledgments

Inspired by TheAlgorithms/Python repo
Built with love using open-source tools
