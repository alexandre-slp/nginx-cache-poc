"""
RPaaS test app
"""
import flask
import logging
from utils import logger_config
from api import routes

try:
    app_name = 'rpaas_test'
    APP = flask.Flask(app_name)
    # Setup Logger
    logger_config.configure_logger(APP, app_name)

    # Setup Routes
    routes.mount_routes(APP)

except Exception as exc:
    logging.critical(f'Exception occurred, exception={exc}')
