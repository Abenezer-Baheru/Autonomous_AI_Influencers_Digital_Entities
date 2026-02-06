# skill_download_youtube

Purpose: Download a YouTube (or similar) video and stage it for processing.

Input (JSON):
{
  "url": "string (video url)",
  "max_resolution": "string (e.g. 1080p)",
  "output_path": "string (optional, default=artifacts/videos/)"
}

Output (JSON):
{
  "status": "ok|error",
  "result": {"file_path": "string", "duration_s": 0.0},
  "confidence": 1.0
}

Notes: Respect platform TOS. Implementers should return deterministic metadata for downstream skills.
