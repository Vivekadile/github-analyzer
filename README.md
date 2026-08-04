# GitHub Repository Analyzer

An AI-powered application that allows users to chat with any public GitHub repository using Retrieval-Augmented Generation (RAG).

Instead of manually searching through hundreds of source files, users can simply paste a GitHub repository URL and ask natural language questions about the codebase.

---

## Features

- Analyze any public GitHub repository
- Clone repositories automatically
- Scan and process source code files
- Generate semantic embeddings
- Store embeddings in ChromaDB
- Retrieve relevant code using vector search
- Generate contextual answers using Groq LLM
- REST API built with FastAPI
- Interactive frontend built with React

---

## Tech Stack

### Backend

- Python
- FastAPI
- ChromaDB
- Sentence Transformers
- LangChain Text Splitters
- Groq API

### Frontend

- React
- Vite
- Tailwind CSS
- Axios

---

## Architecture

```text
                GitHub Repository
                        │
                        ▼
                Clone Repository
                        │
                        ▼
                  Scan Source Files
                        │
                        ▼
                    Read Files
                        │
                        ▼
                  Chunk Source Code
                        │
                        ▼
              Generate Embeddings
                        │
                        ▼
                    ChromaDB
                        │
                        ▼
                  Retrieve Chunks
                        │
                        ▼
                 Prompt Generation
                        │
                        ▼
                    Groq LLM
                        │
                        ▼
                   Final Response
```

---

## Project Structure

```text
github-analyzer/

├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── github/
│   │   ├── rag/
│   │   ├── services/
│   │   └── main.py
│   │
│   ├── repositories/
│   ├── chroma_db/
│   └── requirements.txt
│
└── frontend/
    ├── src/
    ├── public/
    └── package.json
```

---

## API Endpoints

### Analyze Repository

```http
POST /analyze
```

Request

```json
{
    "github_url":"https://github.com/langchain-ai/langchain.git"
}
```

---

### Ask Question

```http
POST /ask
```

Request

```json
{
    "question":"What is BaseChatModel?"
}
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/<your-username>/github-analyzer.git

cd github-analyzer
```

---

### Backend

```bash
cd backend

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

Create a `.env` file

```text
GROQ_API_KEY=your_api_key
```

Run backend

```bash
uvicorn app.main:app --reload --port 7000
```

---

### Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## Workflow

1. Paste a GitHub repository URL.
2. The repository is cloned locally.
3. Source code files are scanned.
4. Files are split into semantic chunks.
5. Embeddings are generated.
6. Embeddings are stored in ChromaDB.
7. User asks questions.
8. Relevant chunks are retrieved.
9. Groq LLM generates an answer grounded in repository context.

---

## Current Features

- Repository cloning
- Repository scanning
- Source code chunking
- Embedding generation
- Vector search
- Retrieval-Augmented Generation (RAG)
- FastAPI backend
- React frontend
- Swagger API documentation

---

## Future Improvements

- Background repository indexing
- Streaming LLM responses
- Authentication
- Repository caching
- Syntax highlighted code references
- Multi-repository support
- Docker deployment
- Cloud deployment

---

## Demo

Coming Soon

---

## Author

**Beeru**

B.Tech Electronics & Computer Engineering

Machine Learning & Generative AI Enthusiast

GitHub: https://github.com/Vivekadile