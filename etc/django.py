import os

dirct = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONFIG = {
    'mode': 'wsgi',
    'working_dir': dirct + '/ask',
    'args': (
        '--bind=0.0.0.0:8000',
        '--workers=16',
        '--timeout=60',
        'ask.wsgi:application',
    ),
}