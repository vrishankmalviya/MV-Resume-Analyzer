````markdown
# 🤖 MV Resume Analyzer using RAG & LLM

An AI-powered Resume Analyzer built using Retrieval-Augmented Generation (RAG), LangChain, FAISS, OpenAI GPT,OpenAI GPT and Gradio.

This application allows users to upload a resume PDF and compare it against a job description to receive intelligent recruiter-style analysis including:

- 📊 Match Score
- ✅ Matching Skills
- ❌ Missing Skills
- 💡 Resume Improvement Suggestions
- 🧠 Custom Recruiter Queries

---

# 🚀 Live Demo

https://mv-resume-analyzer-1.onrender.com/

---

# 📌 Features

✅ Upload Resume PDF  
✅ AI-Powered Resume Analysis  
✅ RAG-Based Semantic Retrieval  
✅ Dynamic Prompt Routing  
✅ Custom Query Support  
✅ Match Score Generation  
✅ Recruiter-Style Feedback  
✅ Interactive Gradio UI  

---

# 🧠 Tech Stack

| Technology | Usage |
|---|---|
| Python | Backend Development |
| LangChain | RAG Pipeline |
| FAISS | Vector Database |
| OpenAI GPT-4o-mini | LLM Response Generation |
| HuggingFace Embeddings | Semantic Embeddings |
| Gradio | Frontend UI |
| PyPDF | PDF Processing |

---

# 🏗️ Project Architecture


Resume PDF + Job Description
              ↓
         PDF Loading
              ↓
         Text Chunking
              ↓
      Embedding Generation
              ↓
      FAISS Vector Storage
              ↓
       Semantic Retrieval
              ↓
        Prompt Routing
              ↓
         OpenAI GPT
              ↓
       Structured Response
              ↓
           Gradio UI
````

---

# 📂 Project Structure

```text
AI_JOB_RAG/
│
├── backend.py
├── ui.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone <your_repo_link>
cd MV_Resume_Analyzer
```

---

## 2️⃣ Create Virtual Environment

```bash
py -3.10 -m venv .anv
```

---

## 3️⃣ Activate Environment

### Windows

```bash
.anv\Scripts\activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key
```

---

# ▶️ Run Application

```bash
python ui.py
```

---

# 🧠 How It Works

### 1. Resume Upload

The user uploads a resume PDF and enters a job description.

### 2. PDF Processing

The resume is loaded and split into smaller chunks using LangChain text splitters.

### 3. Embedding Generation

Chunks are converted into vector embeddings using OpenAi embedding model.

### 4. Vector Database

Embeddings are stored in a FAISS vector database for semantic search.

### 5. Retrieval-Augmented Generation (RAG)

Relevant chunks are retrieved based on the selected task or custom query.

### 6. Prompt Routing

Task-specific prompts are dynamically generated for:

* Match Score
* Matching Skills
* Missing Skills
* Suggestions
* Full Analysis
* Custom Queries

### 7. LLM Analysis

OpenAI GPT generates recruiter-style insights using retrieved resume context.

---

# 🎯 Supported Analysis Types

* Full Analysis
* Match Score
* Matching Skills
* Missing Skills
* Suggestions
* Custom Recruiter Queries

---

# 🔥 Key Concepts Implemented

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Databases
* Prompt Engineering
* Dynamic Prompt Routing
* LLM Integration
* Embedding Models
* Context Injection
* Gradio UI Development

---

# 📈 Future Improvements

* Multi-Resume Comparison
* ATS Compatibility Score
* Resume Ranking System
* Streaming Responses
* Authentication System
* Chat Memory
* Structured JSON Output

---

# 🚀 Deployment

This project can be deployed on:

* Render
* Hugging Face Spaces
* AWS
* Azure

---

# 📸 Screenshots

![alt text](<Screenshot 2026-05-07 152559.png>)

---

# 📄 License

This project is built for educational and portfolio purposes.

