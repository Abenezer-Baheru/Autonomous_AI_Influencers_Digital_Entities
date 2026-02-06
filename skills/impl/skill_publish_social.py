def run(params: dict) -> dict:
    """Minimal stub: simulate publishing and return a post id."""
    platform = params.get('platform', 'twitter')
    content = params.get('content', {})
    return {
        'status': 'ok',
        'result': {'post_id': f'std-{platform}-12345', 'url': f'https://{platform}.example/post/12345'},
        'confidence': 0.95,
    }
