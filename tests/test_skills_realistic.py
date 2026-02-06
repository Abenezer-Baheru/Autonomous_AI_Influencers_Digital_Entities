import os
import pytest
from importlib import import_module
from pathlib import Path


def test_download_youtube_dry_run():
    mod = import_module('skills.impl.skill_download_youtube')
    out_dir = 'artifacts/videos/test_dry'
    res = mod.run({'url': 'https://youtu.be/example', 'output_path': out_dir, 'dry_run': True})
    assert res.get('status') == 'ok'
    fp = res['result']['file_path']
    assert Path(fp).exists()


@pytest.mark.skipif(os.environ.get('RUN_REAL_SKILLS_TESTS') != '1', reason='real skill tests disabled')
def test_download_youtube_real():
    pytest.importorskip('yt_dlp')
    mod = import_module('skills.impl.skill_download_youtube')
    # This will attempt a real download; only run in controlled environments
    res = mod.run({'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'output_path': 'artifacts/videos/real', 'dry_run': False})
    assert res.get('status') == 'ok'


def test_transcribe_dry_run():
    mod = import_module('skills.impl.skill_transcribe_audio')
    res = mod.run({'file_path': 'artifacts/videos/example.mp4', 'dry_run': True})
    assert res.get('status') == 'ok'
    assert 'transcript' in res['result']


@pytest.mark.skipif(os.environ.get('RUN_REAL_SKILLS_TESTS') != '1', reason='real skill tests disabled')
def test_transcribe_real():
    pytest.importorskip('whisper')
    mod = import_module('skills.impl.skill_transcribe_audio')
    res = mod.run({'file_path': 'artifacts/videos/example.mp4', 'dry_run': False})
    assert res.get('status') == 'ok'


def test_publish_dry_run():
    mod = import_module('skills.impl.skill_publish_social')
    res = mod.run({'platform': 'twitter', 'content': {'text': 'hello'}, 'dry_run': True})
    assert res.get('status') == 'ok'


@pytest.mark.skipif(os.environ.get('RUN_REAL_SKILLS_TESTS') != '1', reason='real skill tests disabled')
def test_publish_real():
    # Real connectors are not implemented; this test is a placeholder for integration
    pytest.skip('No real connectors configured')
