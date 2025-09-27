# 🌱 Genesis v2 — Life DB + GMQL + Rosetta

**SQL standardized data. GMQL standardizes memory.**

Genesis v2 is an **AI-native memory database kernel**.  
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
```sql
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
- **[GMQL](../GMQL)** — query language for memory  
- **[LifeDB](../LifeDB)** — memory layer (SQLite → pgvector)  
- **[Rosetta](../Rosetta)** — privacy, consent, audit layer  
- **[GGA](../GGA)** — Genesis General Algebra  
- **[GAA](../GAA)** — Genesis Agent Algebra  
- **[Genesis-algebra](../Genesis-algebra)** — connects GGA and GAA  
- **[Genesis-Rosetta](../Genesis-Rosetta)** — manifest / whitepaper  

## 🚀 Reference Template

📂 **[GCS](https://github.com/drazenco/GCS)** — starter kit for all new repos:  
- OpenAPI + JSON Schema  
- FastAPI reference server (SQLite)  
- Conformance kit (STORE/RECALL/FORGET/CONSENT/EXPORT tests)  
- Journal Bot demo (GDPR use-case)  
- Docker Compose + Makefile

- 
## 📜 License

MIT License — free to use, fork, and contribute.

⚠️ Developer Preview — not production ready.


