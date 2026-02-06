# Skills — Project Chimera

This directory defines runtime "Skills" that agents call to perform concrete actions. Skills are lightweight, well-documented capability contracts (Input/Output) that can be implemented by worker processes or other MCP servers.

Required skills (initial):
- `skill_download_youtube` — Download and stage video assets.
- `skill_transcribe_audio` — Transcribe audio to text and produce timestamps.
- `skill_publish_social` — Publish prepared posts/videos to social platforms.

Each skill MUST provide:
- Name: `skill_<name>`
- Input contract: JSON schema describing required params.
- Output contract: JSON schema describing result, `status` and `confidence`.

Place implementations or wrappers under `skills/impl/` when available.
