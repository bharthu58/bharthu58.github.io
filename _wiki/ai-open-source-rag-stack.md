---
layout: page
title: "AI — Open Source RAG Stack"
---



## Overview

The open-source RAG (Retrieval-Augmented Generation) stack has a layered architecture. Each layer has multiple tool options — mix and match based on your requirements.

---

## The 7-Layer Stack

### Layer 1 — Ingest / Data Processing
Get data into the pipeline: chunk, clean, prepare.

| Tool | Notes |
|---|---|
| **Kubeflow** | ML pipeline orchestration |
| **Apache Airflow** | General-purpose workflow orchestration |
| **Apache Nifi** | Data flow automation |
| **LangChain Document Loaders** | 100+ document type loaders |
| **Haystack Pipelines** | RAG-first pipeline framework |
| **OpenSearch** | Search and ingest |

### Layer 2 — Embedding Model
Convert text chunks to vector representations.

| Tool | Notes |
|---|---|
| **HuggingFace Transformers** | Wide model selection, local or hosted |
| **LLMWare** | Enterprise-focused embedding |
| **Nomic** | Long-context embeddings |
| **Sentence Transformers** | Lightweight, fast, widely used |
| **JinaAI** | Multi-modal embeddings |
| **Cognita** | Managed embedding service |

### Layer 3 — Retrieval & Ranking
Find the most relevant chunks for a query.

| Tool | Notes |
|---|---|
| **FAISS** | Facebook's fast similarity search (local) |
| **Haystack Retrievers** | Modular retrieval components |
| **Weaviate Hybrid Search** | Dense + sparse hybrid retrieval |
| **Elasticsearch kNN** | Vector search on familiar stack |
| **Jina AI Rerankers** | Cross-encoder reranking for precision |

### Layer 4 — Vector Database
Store and query embeddings at scale.

| Tool | Notes |
|---|---|
| **Weaviate** | Hybrid search, multi-modal, self-hostable |
| **Milvus** | High-performance, cloud-native |
| **pgVector** | PostgreSQL extension — use existing DB |
| **Chroma** | Lightweight, local-first, easy to start |
| **Pinecone** | Managed cloud, production-ready |

### Layer 5 — LLMs
The generative component that produces answers.

| Tool | Notes |
|---|---|
| **LLaMA** (Meta) | Most widely deployed open model family |
| **Mistral** | Fast, strong at coding and reasoning |
| **Gemma** (Google) | Lightweight, on-device capable |
| **Phi-2** (Microsoft) | Small but capable, edge deployment |
| **DeepSeek** | Strong coding, low cost |
| **Qwen** (Alibaba) | Multi-lingual, competitive performance |

### Layer 6 — LLM Frameworks
Orchestrate retrieval + generation + memory.

| Tool | Notes |
|---|---|
| **LangChain** | Most popular, widest ecosystem |
| **Haystack** | Production-grade RAG-first framework |
| **LlamaIndex** | Data framework, strong indexing/querying |
| **HuggingFace** | Model hub + inference infrastructure |
| **Semantic Kernel** | Microsoft's enterprise AI SDK |

### Layer 7 — Frontend Frameworks
Build the user-facing interface.

| Tool | Notes |
|---|---|
| **Next.js** | Full-stack React, production-ready |
| **SvelteKit** | Lightweight, fast |
| **Streamlit** | Rapid Python UI prototyping for AI apps |
| **Vue.js** | Progressive, flexible frontend |

---

## Minimal Stack to Start

For a quick proof of concept:
- **Ingest:** LangChain Document Loaders
- **Embedding:** Sentence Transformers (local) or OpenAI Ada
- **Vector DB:** Chroma (local, zero config)
- **LLM:** Mistral or LLaMA via Ollama (local) or Claude API
- **Framework:** LlamaIndex or LangChain
- **Frontend:** Streamlit

For production:
- Replace Chroma with Weaviate or Pinecone
- Add Haystack Pipelines for data processing
- Add reranking (Jina AI or Cohere)
- Deploy frontend with Next.js

---

## See Also

- [AI — Agent Frameworks (N8N vs LangGraph)](/wiki/ai-agent-frameworks-n8n-vs-langgraph/) — orchestration layer above the RAG stack
- [AI — Learning Resources & Roadmap](/wiki/ai-learning-resources-roadmap/) — step 14 of GenAI roadmap covers RAG
- [AI — 30-Day Mastery Mind Map](/wiki/ai-30-day-mastery-mind-map/) — custom knowledge systems section
- [LLM Wiki Pattern](/wiki/llm-wiki-pattern/) — uses a compiled wiki instead of RAG — an alternative architecture

