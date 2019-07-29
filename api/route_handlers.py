"""
Handle routes
"""
import time, random
from flask import request, jsonify, Response
from settings import THREAD_DATA
from utils import helpers, logger_config


LOG = logger_config.get_logger()


def rand_int_a() -> (Response, int):
    """
    Route that generates a random integer
    :return:
        200 - Succeeded
        400 - Bad Request
        405 - Method Not Allowed
        500 - Error Accessing Google
    """
    THREAD_DATA.start = int(round(time.time() * 1000))
    rand_int = random.randint(0, 10)
    response = {'random int A': rand_int}
    LOG.info(f'Generated random int (A): {rand_int}')
    request_time = int(round(time.time() * 1000)) - THREAD_DATA.start
    status_code = 200
    helpers.log_route_info(request, request_time, status_code)
    return jsonify(response), status_code


def rand_int_b() -> (Response, int):
    """
    Route to check API status.
    :return:
        200 - Succeeded
    """
    THREAD_DATA.start = int(round(time.time() * 1000))
    rand_int = random.randint(10, 20)
    response = {'random int B': rand_int}
    LOG.debug(f'Generated random int (B): {rand_int}')
    request_time = int(round(time.time() * 1000)) - THREAD_DATA.start
    status_code = 200
    helpers.log_route_info(request, request_time, status_code)
    return jsonify(response), status_code
