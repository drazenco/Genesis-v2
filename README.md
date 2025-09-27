
# 🌱 Genesis v2 — Life DB + GMQL + Rosetta

[![Build](https://github.com/drazenco/Genesis-v2/actions/workflows/python-tests.yml/badge.svg)](https://github.com/drazenco/Genesis-v2/actions/workflows/python-tests.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Status: Developer Preview](https://img.shields.io/badge/status-developer--preview-orange)

**Genesis v2** is an **AI-native memory database kernel**.  
It provides a durable, portable, and privacy-first memory layer for AI agents and applications, powered by the **Genesis Memory Query Language (GMQL)**.

---

## ✨ Why it matters

By 2030, a personal AI without durable memory will feel like a computer without a disk.  
Genesis v2 introduces:

- 📖 **GMQL** → SQL-like language for memory (`STORE`, `RECALL`, `FORGET`, `CONSENT`)
- 🗂 **Life DB** → Memory kernel (`journal`, `team_log`, `health_diary`)
- 🔎 **Rosetta** → Vision: memory with privacy and consent as defaults

---

## 🚀 Quickstart

```bash
git clone https://github.com/drazenco/Genesis-v2.git
cd Genesis-v2
pip install -r requirements.txt
uvicorn src.api.main:app --reload
```

### Example GMQL

```
STORE INTO journal EVENT(type="note", text="First memory in Genesis v2!")
RECALL FROM journal WHERE type="note"
```

---

## 📦 Features (v0.1 — Developer Preview)

- GMQL core commands: `STORE`, `RECALL`, `FORGET`
- SQLite backend with default collections (`journal`, `team_log`, `health_diary`)
- Consent & Forget API (privacy by design)
- OpenAI embeddings integration (semantic recall)
- CLI + REST API prototypes

---

## 🛠 Roadmap

- **v0.5** → Postgres driver, Query planner, Consent logs  
- **v1.0** → Multi-driver, AI-native RAG bridges, production-ready Life DB  
- **Beyond** → GMQL RFCs, community governance, Genesis Studio (UI)

---

## 🌐 Ecosystem

Genesis-v2 is part of the wider **Genesis Core Standard (GCS)** ecosystem:

```
                ┌──────────────┐
                │  Genesis-v2  │   ← central hub (engine + API)
                └───────┬──────┘
                        │
        ┌───────────────┼────────────────┐
        │               │                │
 ┌────────────┐   ┌────────────┐   ┌───────────────┐
 │   GMQL     │   │   LifeDB   │   │    Rosetta    │
 │ query lang │   │ memory core│   │ privacy/consent│
 └─────┬──────┘   └──────┬─────┘   └──────┬────────┘
       │                 │                │
       ▼                 ▼                ▼
 ┌────────────┐   ┌────────────┐   ┌───────────────┐
 │    GGA     │   │    GAA     │   │ Genesis-Rosetta│
 │ gen algebra│   │ agent alg. │   │ manifest/white │
 └────────────┘   └────────────┘   └───────────────┘
```

- **[GCS](https://github.com/drazenco/GCS)** — core standard & conformance kit  
- **[GMQL](https://github.com/drazenco/GMQL)** — query language for memory  
- **[LifeDB](https://github.com/drazenco/LifeDB)** — memory layer (SQLite → pgvector)  
- **[Rosetta](https://github.com/drazenco/Rosetta)** — privacy, consent, audit layer  
- **[GGA](https://github.com/drazenco/GGA)** — Genesis General Algebra  
- **[GAA](https://github.com/drazenco/GAA)** — Genesis Agent Algebra  
- **[Genesis-algebra](https://github.com/drazenco/Genesis-algebra)** — bridges GGA and GAA  
- **[Genesis-Rosetta](https://github.com/drazenco/Genesis-Rosetta)** — manifest / whitepaper  

---

## ✅ Conformance

Genesis-v2 implements **GCS v0.1** invariant operators:

- `STORE` — store memory  
- `RECALL` — retrieve memory  
- `FORGET` — right to be forgotten  
- `CONSENT` — consent management  
- `EXPORT` — data transfer (NDJSON)

This ensures compatibility with the Genesis Core Standard and provides a stable base for future versions (v0.2 → v1.0).

---

## 🚀 Reference Template

📂 **[GCS](https://github.com/drazenco/GCS)** — starter kit for all new repos:

- OpenAPI + JSON Schema  
- FastAPI reference server (SQLite)  
- Conformance kit (STORE/RECALL/FORGET/CONSENT/EXPORT tests)  
- Journal Bot demo (GDPR use-case)  
- Docker Compose + Makefile  

---

## 📜 License

MIT License — free to use, fork, and contribute.  
⚠️ Developer Preview — not production ready.
