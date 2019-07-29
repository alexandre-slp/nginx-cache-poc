"""
All constants
"""
import os
import threading

# Configure log
LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
FORMAT = '%(asctime)s [%(levelname)s]: request_id=%(request_id)s %(message)s'
DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S%z'

# App Google OAUTH
HOST = os.environ.get('HOST', '0.0.0.0')
PORT = int(os.environ.get('PORT', '8000'))

# Error handlers
THREAD_DATA = threading.local()
