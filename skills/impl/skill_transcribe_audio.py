import os
from pathlib import Path


def _simulate_transcript(file_path: str):
    transcript = f"Simulated transcript for {Path(file_path).name}."
    segments = [{'start_s': 0.0, 'end_s': 5.0, 'text': transcript}]
    return transcript, segments


def run(params: dict) -> dict:
    """Transcribe audio using `whisper` if installed; otherwise support `dry_run` simulation.

    Params:
    - file_path (required)
    - language (optional)
    - timestamp_granularity_s (optional)
    - dry_run (bool, default True)
    """
    file_path = params.get('file_path')
    if not file_path:
        return {'status': 'error', 'result': {'error': 'missing file_path'}, 'confidence': 0.0}

    dry_run = params.get('dry_run', True)
    if dry_run:
        transcript, segments = _simulate_transcript(file_path)
        return {'status': 'ok', 'result': {'transcript': transcript, 'segments': segments}, 'confidence': 0.5}

    # Try whisper (OpenAI) if available
    try:
        import whisper
        model = whisper.load_model('small')
        res = model.transcribe(file_path)
        text = res.get('text', '')
        # coarse segments from timestamps if available
        segments = []
        for seg in res.get('segments', [])[:10]:
            segments.append({'start_s': seg.get('start', 0.0), 'end_s': seg.get('end', 0.0), 'text': seg.get('text', '')})
        return {'status': 'ok', 'result': {'transcript': text, 'segments': segments}, 'confidence': 0.9}
    except Exception as e:
        return {'status': 'error', 'result': {'error': str(e)}, 'confidence': 0.0}
