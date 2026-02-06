# skill_publish_social

Purpose: Publish prepared content to social platforms via MCP bridges or platform APIs.

Input (JSON):
{
  "platform": "string (e.g. twitter, instagram)",
  "content": {"text": "string", "attachments": ["file_path", ...]},
  "schedule_time": "ISO8601 (optional)"
}

Output (JSON):
{
  "status": "ok|error",
  "result": {"post_id": "string", "url": "string"},
  "confidence": 0.0
}

Notes: Implementations MUST return platform-specific identifiers when available and handle rate-limiting gracefully.
