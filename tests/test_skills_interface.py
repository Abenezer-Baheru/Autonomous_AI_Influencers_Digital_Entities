import pytest
from importlib import import_module


def test_skill_download_youtube_interface():
    """Spec: `skill_download_youtube` must be implemented as a Python module
    exposing a `run(params)` function that returns a dict with `status` and `confidence`.
    """
    mod = import_module('skills.impl.skill_download_youtube')
    assert hasattr(mod, 'run'), 'skill_download_youtube must implement run(params)'
    res = mod.run({
        'url': 'https://youtu.be/example',
        'output_path': 'artifacts/videos/'
    })
    assert isinstance(res, dict)
    assert res.get('status') in ('ok', 'error')
    assert 'confidence' in res


def test_skill_transcribe_audio_interface():
    mod = import_module('skills.impl.skill_transcribe_audio')
    assert hasattr(mod, 'run'), 'skill_transcribe_audio must implement run(params)'
    res = mod.run({
        'file_path': 'artifacts/videos/example.mp4',
        'language': 'en'
    })
    assert isinstance(res, dict)
    assert res.get('status') in ('ok', 'error')
    assert 'result' in res


def test_skill_publish_social_interface():
    mod = import_module('skills.impl.skill_publish_social')
    assert hasattr(mod, 'run'), 'skill_publish_social must implement run(params)'
    res = mod.run({
        'platform': 'twitter',
        'content': {'text': 'test post', 'attachments': []}
    })
    assert isinstance(res, dict)
    assert res.get('status') in ('ok', 'error')
    assert 'result' in res
