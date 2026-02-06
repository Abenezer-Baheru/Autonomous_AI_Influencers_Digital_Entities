# skill_transcribe_audio

Purpose: Produce a time-aligned transcript and speaker segments from an audio/video file.

Input (JSON):
{
  "file_path": "string (local path to audio/video)",
  "language": "string (e.g. en)",
  "timestamp_granularity_s": 1.0
}

Output (JSON):
{
  "status": "ok|error",
  "result": {
    "transcript": "string",
    "segments": [{"start_s":0.0, "end_s":1.2, "text":"..."}]
  },
  "confidence": 0.0
}

Notes: Output `segments` should be precise to allow clip-creation by downstream workers.
