"""
Define all app routes
"""

import flask
from api import route_handlers
from utils.errors_handler import invalid_request, method_not_allowed, internal_server_error


def mount_routes(app: flask.Flask):
    """
    Mount routes and error routes to app
    :param app: App instance
    :return:
    """
    app.add_url_rule(rule='/api/v1/rand_int_a',
                     view_func=route_handlers.rand_int_a,
                     endpoint=route_handlers.rand_int_a.__name__,
                     methods=['GET'])

    app.add_url_rule(rule='/api/v1/rand_int_b',
                     view_func=route_handlers.rand_int_b,
                     endpoint=route_handlers.rand_int_b.__name__,
                     methods=['GET'])

    app.register_error_handler(400, invalid_request)
    app.register_error_handler(405, method_not_allowed)
    app.register_error_handler(500, internal_server_error)
