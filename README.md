# PalmMind AI RAG Assignment

A Retrieval-Augmented Generation (RAG) backend built with **FastAPI** that supports document ingestion, conversational question answering, multi-turn chat memory, and an AI-powered interview booking workflow.

---

## Features

### Document Ingestion API

- Upload `.pdf` and `.txt` documents
- Extract text from uploaded files
- Select between two chunking strategies
- Generate embeddings
- Store embeddings in Qdrant
- Save document metadata in SQLite

### Conversational RAG API

- Custom RAG pipeline (without RetrievalQAChain)
- Semantic retrieval using Qdrant
- Query rewriting for follow-up questions
- Multi-turn conversations
- Redis (Memurai) chat memory

### Interview Booking Agent

- Intent detection
- Multi-turn booking conversation
- Collects:
  - Name
  - Email
  - Interview Date
  - Interview Time
- Stores booking state in Redis
- Stores completed bookings in SQLite

---

# Tech Stack

- FastAPI
- Python
- Sentence Transformers
- Qdrant
- SQLite
- Redis (Memurai)
- OpenRouter API
- Gemini 2.5 Flash

---

# Project Structure

```
app/
│
├── api/
│   ├── upload.py
│   └── chat.py
│
├── database/
│   └── database.py
│
├── schemas/
│
├── services/
│   ├── booking.py
│   ├── booking_agent.py
│   ├── embeddings.py
│   ├── intent.py
│   ├── llm.py
│   ├── parser.py
│   ├── qdrant.py
│   ├── query_rewriter.py
│   ├── redis_memory.py
│   ├── retrieval.py
│   └── chunking.py
│
├── main.py
│
sample_data/
│
└── test data.pdf
```

---

# Setup

## 1. Clone the repository

```bash
git clone <repository-url>
cd palmmind-ai-rag-assignment
```

---

## 2. Create a virtual environment

Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS

```bash
python -m venv .venv
source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure environment variables

Create a `.env` file in the project root.

```env
OPENROUTER_API_KEY=YOUR_OPENROUTER_API_KEY
```

---

## 5. Start Qdrant

Run a local Qdrant instance.

### Option 1 (Windows Executable)

Run `qdrant.exe`.

### Option 2 (Docker)

```bash
docker run -p 6333:6333 qdrant/qdrant
```

The application expects Qdrant to be available at:

```
http://localhost:6333
```

## 6. Start Redis

Start your local Redis server (Memurai).

---

## 7. Run the FastAPI server

```bash
uvicorn app.main:app --reload
```

---

## 8. Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# Testing the Application

## Step 1 — Upload a document

Use the **Upload API** to upload:

```
sample_data/test data.pdf
```

This ingests the document into Qdrant and stores its metadata.

---

## Step 2 — Test the RAG API

Example request:

```json
{
    "session_id": "rag_demo",
    "question": "What is FastAPI?"
}
```

Example follow-up:

```json
{
    "session_id": "rag_demo",
    "question": "Explain it in simple words."
}
```

---

## Step 3 — Test Interview Booking

Start a booking conversation:

```json
{
    "session_id": "booking_demo",
    "question": "I want to schedule an interview."
}
```

Continue the conversation:

```json
{
    "session_id": "booking_demo",
    "question": "John Doe"
}
```

```json
{
    "session_id": "booking_demo",
    "question": "john@example.com"
}
```

```json
{
    "session_id": "booking_demo",
    "question": "25 August 2026"
}
```

```json
{
    "session_id": "booking_demo",
    "question": "2 PM"
}
```

The booking will be stored in SQLite upon completion.

---

# Architecture

```
                User
                  │
                  ▼
            FastAPI Backend
                  │
                  ▼
          Intent Detection
         ┌────────┴────────┐
         │                 │
         ▼                 ▼
 Interview Booking      RAG Pipeline
         │                 │
         ▼                 ▼
 Redis Booking      Query Rewriter
     State               │
         │               ▼
         │         Vector Search
         │           (Qdrant)
         │               │
         ▼               ▼
 SQLite Booking        LLM
```

---

# Database

SQLite stores:

- Uploaded document metadata
- Interview bookings

---

# Notes

- Qdrant must be running before starting the application.
- Redis (Memurai) must be running for chat memory and booking state.
- A valid OpenRouter API key is required.
- Upload the sample PDF before testing the RAG endpoint.

---

# Author

**Rohit Dhourali**