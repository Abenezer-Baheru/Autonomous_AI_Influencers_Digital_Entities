import os
import shutil
import subprocess
from pathlib import Path


def run(params: dict) -> dict:
    """Download a video using `yt_dlp` if available, otherwise simulate when `dry_run`.

    Supported params:
    - url (required)
    - output_path (directory or file path)
    - max_resolution (optional)
    - dry_run (bool, default True) -> when True do not require network or external deps
    """
    url = params.get('url')
    if not url:
        return {'status': 'error', 'result': {'error': 'missing url'}, 'confidence': 0.0}

    output_path = params.get('output_path', 'artifacts/videos/')
    dry_run = params.get('dry_run', True)

    # If dry_run, create a placeholder file and return deterministic metadata
    if dry_run:
        Path(output_path).mkdir(parents=True, exist_ok=True)
        file_path = str(Path(output_path) / 'downloaded_example.mp4') if Path(output_path).is_dir() else output_path
        # create an empty placeholder if not exists
        try:
            Path(file_path).parent.mkdir(parents=True, exist_ok=True)
            if not Path(file_path).exists():
                Path(file_path).write_bytes(b'')
        except Exception:
            pass
        return {
            'status': 'ok',
            'result': {'file_path': file_path, 'duration_s': 60.0, 'source_url': url},
            'confidence': 0.6,
        }

    # Try using yt_dlp Python API
    try:
        import yt_dlp

        # prepare output template
        out_template = output_path
        if Path(output_path).is_dir():
            out_template = str(Path(output_path) / '%(id)s.%(ext)s')

        ydl_opts = {'outtmpl': out_template}
        if params.get('max_resolution'):
            # yt_dlp format selection could be more complex; leave to implementers
            pass

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            # attempt to find downloaded filename
            filename = ydl.prepare_filename(info)
            duration = info.get('duration') if isinstance(info, dict) else None
            return {'status': 'ok', 'result': {'file_path': filename, 'duration_s': duration or 0.0, 'source_url': url}, 'confidence': 0.9}
    except Exception:
        # as a safe fallback, try shelling out to yt-dlp CLI if installed
        try:
            out_dir = output_path if Path(output_path).is_dir() else str(Path(output_path).parent)
            Path(out_dir).mkdir(parents=True, exist_ok=True)
            cmd = ['yt-dlp', '-o', str(Path(out_dir) / '%(id)s.%(ext)s'), url]
            subprocess.run(cmd, check=True)
            # best-effort: pick the newest file in out_dir
            files = sorted(Path(out_dir).glob('*'), key=lambda p: p.stat().st_mtime, reverse=True)
            if files:
                f = files[0]
                return {'status': 'ok', 'result': {'file_path': str(f), 'duration_s': 0.0, 'source_url': url}, 'confidence': 0.7}
        except Exception as e:
            return {'status': 'error', 'result': {'error': str(e)}, 'confidence': 0.0}

    return {'status': 'error', 'result': {'error': 'no downloader available'}, 'confidence': 0.0}
