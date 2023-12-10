import logging
from datetime import datetime
from io import BytesIO
from logging.handlers import RotatingFileHandler
from flask import request


class LogMiddleware:
    def __init__(self, app):
        self.app = app
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(RotatingFileHandler('./logs/server.log', maxBytes=10000, backupCount=1))

    def __call__(self, environ, start_response):
        input_stream = environ.get('wsgi.input')
        length = int(environ.get('CONTENT_LENGTH') or 0)
        body = ''
        if length > 0:
            input_stream = BytesIO(input_stream.read(length))
            body = input_stream.getvalue().decode('utf-8')
            input_stream.seek(0)
            environ['wsgi.input'] = input_stream

        def log_requests(status, headers, *args):
            timestamp = datetime.utcnow().strftime('%d/%b/%Y %H:%M:%S')
            self.logger.info(f"{request.remote_addr} - [{timestamp}] - {request.method} {request.url} - {status}")
            if length>0:
                self.logger.info(f"Body:{body}")
            return start_response(status, headers, *args)

        return self.app(environ, log_requests)
