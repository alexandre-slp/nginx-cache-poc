"""
This function is responsible for configuring all settings from the logger
"""
import sys
import logging
import uuid
import flask
from settings import LOG_LEVEL, FORMAT, DATE_TIME_FORMAT


class RequestIdFilter(logging.Filter):
    """
    Class purpose is to add request_id in the logger message pattern
    """
    def filter(self, record: logging.LogRecord) -> bool:
        """
        Add request_id to logging message if available
        :param record:
        :return:
        """
        if not getattr(flask.g, 'request_id', None):
            if flask.request.headers.get('X-Request-ID'):
                flask.g.request_id = flask.request.headers.get('X-Request-ID')
            else:
                flask.g.request_id = f'{uuid.uuid4()}'

        record.request_id = flask.g.request_id
        return True


# pylint: disable=W0603
APP = ''
NAME = 'rpaas_test'


def configure_logger(app_instance: flask.Flask, app_name: str):
    """
    Responsible for all app's Logger setup
    :param app_instance: Flask app
    :param app_name: App name
    """
    global APP, NAME
    APP = app_instance
    NAME = app_name

    # Configure basic log level for all loggers
    for logger_name in APP.logger.manager.loggerDict:
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.WARNING)

    # Logger setup
    logger = logging.getLogger(NAME)
    logger.setLevel(logging.getLevelName(LOG_LEVEL))

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.getLevelName(LOG_LEVEL))
    console_handler.addFilter(RequestIdFilter())

    formatter = logging.Formatter(fmt=FORMAT, datefmt=DATE_TIME_FORMAT)

    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    APP.logger = logger


def get_logger() -> logging.Logger:
    """
    Returns the app's Logger
    :return: App's Logger
    """
    global NAME
    return logging.getLogger(NAME)
