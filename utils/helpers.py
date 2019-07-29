"""
Helper functions
"""
from flask import request
from utils import logger_config

LOG = logger_config.get_logger()


def log_route_info(flask_request: request,
                   request_time: int,
                   status_code: int,
                   error_message=''):
    """
    Log routes report before returning an answer
    :param flask_request: Flask request context
    :param request_time: Request time
    :param status_code: Status code
    :param error_message: Error message
    """
    LOG.info(f'status_code={status_code}, '
             f'method={flask_request.method}, '
             f'path={flask_request.full_path}, '
             f'request_timems={request_time:.0f}, '
             f'env={flask_request.environ.get("SERVER_PROTOCOL", " - ")}, '
             f'size={flask_request.environ.get("CONTENT_LENGTH", " - ")}, '
             f'referer={flask_request.url_root}, '
             f'remote_addr={flask_request.remote_addr}, '
             f'user_agent={flask_request.user_agent}' +
             f'{f", error_message={error_message}" if error_message else ""}')
