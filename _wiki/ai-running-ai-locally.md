---
layout: page
title: "AI — Running AI Locally"
---

# AI — Running AI Locally

Setup guide for running LLM models locally, from a basic laptop through a multi-user team server.

See also: [AI — Foundational Concepts](/wiki/ai-foundational-concepts/), [AI — Learning Resources & Roadmap](/wiki/ai-learning-resources-roadmap/)

---

## Why Run Locally

- **Privacy** — prompts stay on your machine; no third-party data policy exposure
- **Cost** — no per-token billing; one-time hardware cost amortises over heavy use
- **Offline** — no internet dependency, no rate limits, no service outages
- **It works now** — Qwen3, Llama 4, DeepSeek, Gemma 3 handle most everyday tasks on consumer hardware

---

## The Critical Hardware Metric: VRAM

VRAM (GPU memory) is what matters — not CPU or total RAM. The model must fit in VRAM during inference. If it overflows to system RAM, speed drops from ~35 tokens/sec to ~3 tokens/sec.

**Quick check:** visit `CanIRun.ai` — detects your GPU/CPU/RAM via browser and shows which models your machine can run. No sign-up.

---

## Hardware Tiers and Recommended Setup

### Tier 1: Laptop (8–16GB RAM, no dedicated GPU)

Models that fit:
- 8GB RAM: 3B–7B parameter models (Phi-4 Mini, Mistral 7B — ~4–6GB when loaded)
- 16GB RAM: up to 12B (Gemma 3 12B handles general chat well)

Speed: CPU-only runs at 3–8 tokens/sec — usable for drafting, slow for chat.

**Tool: LM Studio** (`lmstudio.ai`)
- GUI, works on Windows / Mac / Linux
- Searches and downloads models from HuggingFace
- Auto-detects hardware; falls back to CPU if no GPU
- Easiest starting point for non-technical users

Alternative: **GPT4All** — even simpler, fewer model options.

---

### Tier 2: Desktop with Dedicated GPU

| GPU | VRAM | Model range | Speed |
|-----|------|-------------|-------|
| RTX 3060 12GB | 12GB | 7B–8B comfortably | 30–50 tokens/sec |
| RTX 4060 Ti 16GB | 16GB | 7B–13B | 30–50 tokens/sec |
| RTX 3090 / 4090 | 24GB | 30B models; compressed 70B | 40–60 tokens/sec |

**Warning:** avoid the RTX 4060 Ti 8GB — the 8GB VRAM fills up once model + context grows. The 16GB version is worth the premium.

**Tool: Ollama** (CLI)
```bash
ollama run llama3.3    # pulls model if not local, starts chat
```
- Single install, works immediately
- Runs a local API server on port 11434 (OpenAI-compatible)
- Any app that talks to OpenAI's API can point at `localhost:11434` instead

**Optional UI on top of Ollama: Open WebUI** — browser-based chat interface, feels like a proper chat app.

---

### Tier 3: Advanced / Team Use

**Apple Silicon Macs (unified memory)**
- GPU and CPU share the same memory pool — no VRAM ceiling
- Mac Mini M4 (16GB): handles 14B models smoothly
- Mac Studio M3 Ultra (96GB): multiple large models in memory simultaneously
- Best consumer option for large models without a discrete GPU

**vLLM (for serving a team)**
```bash
python -m vllm.entrypoints.openai.api_server --model meta-llama/Llama-3.3-8B
```
- Handles concurrent requests (Ollama doesn't)
- OpenAI-compatible API — drops in as a replacement
- More setup work; right choice when more than one person needs access

---

## Model Format: GGUF

GGUF is the standard format for quantised models on consumer hardware (available on Hugging Face).

| Quantisation | Size vs quality trade-off |
|-------------|--------------------------|
| Q4_K_M | Good balance — recommended starting point |
| Q5_K_M | Better quality, ~25% more memory |
| Q8_0 | Near-original quality, ~2× Q4 memory |

For most local use: **Q4 or Q5**. Q8 if you have VRAM to spare and want maximum fidelity.

---

## Tool Comparison

| Tool | Interface | Best for |
|------|-----------|---------|
| LM Studio | GUI | Laptop / beginner / visual model browser |
| Ollama | CLI + API | GPU desktop / developers / app integration |
| Open WebUI | Browser | Chat UI layer on top of Ollama |
| GPT4All | GUI | Simplest possible local setup |
| vLLM | Server | Team/multi-user deployment |

---

## Known Limitations

- **Quality ceiling** — local models are behind GPT-4o and Claude on complex reasoning and very long documents; the gap narrows quickly each generation
- **Speed on CPU** — 3–8 tokens/sec on a CPU-only laptop; acceptable for drafting, not for interactive chat
- **Manual updates** — new model versions don't auto-install; you pull and switch manually
- **Context window** — most local models cap at 8K–32K tokens vs 200K+ for cloud models

