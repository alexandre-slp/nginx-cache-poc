"""
Handle all errors
"""
import time
from flask import request, jsonify, Response
from settings import THREAD_DATA
from utils import logger_config, helpers

LOG = logger_config.get_logger()


# pylint: disable=W0613, C0103
def invalid_request(e: str) -> (Response, int):
    """
    Handle invalid JSON format error.
    :return: 400 with JSON error message
    """
    request_time = int(round(time.time() * 1000)) - THREAD_DATA.start
    status_code = 400
    helpers.log_route_info(request, request_time, status_code, e)
    LOG.debug(f'content_type={request.content_type}, '
              f'request_data={request.data}')
    return jsonify({'error': f'{e}'}), status_code


# pylint: disable=W0613, C0103
def method_not_allowed(e: str) -> (Response, int):
    """
    Handle Method Not Allowed error.
    :return: 405 with JSON error message
    """
    THREAD_DATA.start = int(round(time.time() * 1000))
    request_time = int(round(time.time() * 1000)) - THREAD_DATA.start
    status_code = 405
    helpers.log_route_info(request, request_time, status_code, e)
    return jsonify({'error': f'{e}'}), status_code


# pylint: disable=W0613, C0103
def internal_server_error(e: str) -> (Response, int):
    """
    Handle error while adding JSON to queue.
    :return: 500 with JSON error message
    """
    request_time = int(round(time.time() * 1000)) - THREAD_DATA.start
    status_code = 500
    helpers.log_route_info(request, request_time, status_code, e)
    return jsonify({"error": f"{e}"}), status_code
