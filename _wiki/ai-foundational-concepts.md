---
layout: page
title: "AI — Foundational Concepts"
domain: "AI / LLM"
---

20 core concepts from neural networks through diffusion models, grouped by conceptual layer.

See also: [AI — Learning Resources & Roadmap](/wiki/ai-learning-resources-roadmap/), [AI — Agent Systems](/wiki/ai-agent-systems/), [AI — Open Source RAG Stack](/wiki/ai-open-source-rag-stack/)

---

## Group 1: Basics

### 1. Neural Networks
Layers of weighted nodes that transform an input signal into a prediction. Each layer learns increasingly abstract representations. A network learns by adjusting weights to minimise prediction error (via backpropagation + gradient descent). Universal approximators — given enough capacity and data, they can learn arbitrary mappings.

### 2. Transfer Learning
Take a model pretrained on a large general dataset, then continue training on a smaller domain-specific dataset. The pretrained weights encode general knowledge (grammar, shapes, concepts); the fine-tuning step specialises that knowledge for the target task. Enables high performance with far less data and compute than training from scratch.

---

## Group 2: The Transformer Stack

### 3. Tokenisation
Text is split into tokens (words, subwords, or characters depending on the vocabulary) and mapped to integer IDs. The vocabulary is built from training data; rare words become multiple tokens. Token count determines cost and context window usage.

### 4. Embeddings
Each token ID is mapped to a dense real-valued vector in a high-dimensional space. Similar concepts cluster nearby. The embedding layer is learned during training — it encodes semantic relationships as geometric distances. The input to all transformer layers.

### 5. Attention
The mechanism that lets each token "look at" every other token in the sequence and weight their relevance. `Attention(Q, K, V) = softmax(QKᵀ/√d_k)V`. Multi-head attention runs multiple attention computations in parallel with different projections, capturing different types of relationships simultaneously. The computational core of the transformer.

### 6. Transformer
Architecture combining multi-head self-attention + feedforward layers + residual connections + layer normalisation. An encoder processes the full input (BERT-style); a decoder generates autoregressively (GPT-style); encoder-decoder does both (T5-style). Parallelisable during training (unlike RNNs) — enabled the scale-up to LLMs.

---

## Group 3: LLMs

### 7. LLM (Large Language Model)
A transformer trained on vast amounts of text (hundreds of billions to trillions of tokens) to predict the next token. Scale produces emergent capabilities not present in smaller models: reasoning, in-context learning, instruction following.

### 8. Context Window
The maximum number of tokens the model can process in a single forward pass (input + output). Everything outside the window is invisible. Larger windows (100K–1M+) enable processing full documents and codebases. Cost and latency scale roughly linearly with context length.

### 9. Temperature
Controls output randomness. At temperature 0 the model deterministically picks the highest-probability token (greedy decoding). At temperature 1 it samples from the distribution. Above 1 increases diversity/creativity at the cost of coherence. For deterministic tasks (classification, code) use low temperature; for creative tasks use 0.7–1.0.

### 10. Hallucination
The model generates confident, fluent, false information. Causes: training data contains contradictions, the model learned to sound plausible rather than to be accurate, no explicit "I don't know" training signal. Mitigation: RAG (ground in retrieved facts), anti-hallucination protocols (confidence labelling), tool use (verify claims against live sources).

---

## Group 4: Training Techniques

### 11. Fine-Tuning
Continue training a pretrained base model on a curated dataset for the target task. Updates all (or selected) model weights. More powerful than prompting alone but requires labelled data and compute. Full fine-tuning is expensive; parameter-efficient methods (LoRA) are preferred.

### 12. RLHF (Reinforcement Learning from Human Feedback)
1. Fine-tune a base model on curated instruction-response pairs (SFT)
2. Train a reward model on human preference rankings of model outputs
3. Use PPO (or similar RL algorithm) to optimise the LLM to maximise reward model score

RLHF is how base models become instruction-following assistants. The reward model captures preferences that are hard to specify explicitly (tone, helpfulness, safety).

### 13. LoRA (Low-Rank Adaptation)
Instead of updating all model weights during fine-tuning, freeze the original weights and inject small trainable low-rank matrices at each layer. Parameters to train: ≪1% of the original model. The original weights are unchanged — LoRA adapters are additive. Multiple adapters can be swapped at inference time for different tasks.

### 14. Quantisation
Reduce the numerical precision of model weights: float32 → float16 → int8 → int4. Shrinks model size (4-bit ≈ 4× smaller than float32) and speeds up inference. Some accuracy loss; Q4/Q5 is the common sweet spot for local deployment. GGUF is the standard format for quantised models on consumer hardware.

---

## Group 5: Prompting and Systems

### 15. Prompt Engineering
Crafting the input (system prompt + user message) to reliably elicit desired output. Key techniques: role assignment ("you are a senior engineer"), few-shot examples, output format specification, explicit constraints. Distinct from context engineering (which controls what information is in context, not just how the instruction is phrased).

### 16. Chain of Thought (CoT)
Instructing the model to reason step-by-step before giving a final answer ("think step by step"). Significantly improves performance on multi-step reasoning, maths, and logical problems. The intermediate reasoning steps serve as "scratch paper" — they allow the model to attend to intermediate results rather than compressing a complex derivation into a single token prediction.

### 17. RAG (Retrieval-Augmented Generation)
At query time, retrieve relevant documents from an external store and inject them into the prompt. Grounds the model's response in specific, current, authoritative content — reducing hallucination and enabling the model to answer questions beyond its training cutoff. The retrieval step is typically semantic (vector search).

### 18. Vector Database
A database optimised for storing and querying high-dimensional embedding vectors by similarity (cosine, dot product, Euclidean). Enables semantic search: find the k nearest embeddings to a query embedding. Core infrastructure for RAG. Examples: Pinecone, Weaviate, Chroma, pgvector (PostgreSQL extension), Qdrant.

### 19. Agents
An LLM + a tool-use loop + memory. The model decides which tool to call, receives results, and continues reasoning until the task is complete. See [AI — Agent Systems](/wiki/ai-agent-systems/) for full pattern coverage.

### 20. Diffusion Models
Generate data by learning to reverse a gradual noising process. Training: add noise to real data in steps. Inference: start from pure noise and denoise step-by-step, guided by a conditioning signal (text prompt). Dominant architecture for image generation (Stable Diffusion, DALL-E, Midjourney) and increasingly for audio and video.
