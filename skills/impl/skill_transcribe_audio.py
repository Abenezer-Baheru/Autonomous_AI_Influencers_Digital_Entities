def run(params: dict) -> dict:
    """Minimal stub: return a simple transcript structure."""
    file_path = params.get('file_path', 'artifacts/videos/example.mp4')
    transcript = "This is a stub transcript."
    segments = [{'start_s': 0.0, 'end_s': 5.0, 'text': transcript}]
    return {
        'status': 'ok',
        'result': {'transcript': transcript, 'segments': segments},
        'confidence': 0.9,
    }
