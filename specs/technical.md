# Technical Specification

API Contracts

- Trend Fetcher (agent -> service)
  - Request: {"sources": ["twitter","reddit","youtube"], "max_items": 50}
  - Response: {"trends": [{"topic": "string", "score": 0.0, "source": "string", "timestamp": "ISO8601"}]}

- Skill Interface (example)
  - Input: {"skill": "skill_name", "params": {...}}
  - Output: {"status": "ok|error", "result": {...}, "confidence": 0.0}

Database schema (high-level)

- videos (id PK, title, created_at, duration, weaviate_ref)
- video_metadata (id PK, video_id FK, key, value, timestamp)

Notes:
- Use PostgreSQL (+Timescale) for telemetry; Weaviate for vector embeddings and RAG queries.
