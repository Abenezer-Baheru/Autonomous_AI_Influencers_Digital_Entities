def run(params: dict) -> dict:
    """Minimal stub: pretend to download and return deterministic metadata.
    """
    url = params.get('url')
    output_path = params.get('output_path', 'artifacts/videos/example.mp4')
    return {
        'status': 'ok',
        'result': {'file_path': output_path, 'duration_s': 60.0, 'source_url': url},
        'confidence': 1.0,
    }
