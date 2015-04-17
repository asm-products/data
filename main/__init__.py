# -*- coding: utf-8 -*-

import settings, wait, log

wait_fors = (
    settings.MONGO_HOST.split(':'),
    (settings.REDIS_HOST, settings.REDIS_PORT)
)
for (host, port) in wait_fors:
    log.info("Waiting for {0}:{1}".format(host, port))
    if not wait.tcp.open(int(port), host, timeout=300):
        raise EnvironmentError("Timeout waiting for {0}:{1}".format(host, port))

from app import create_app
main_app = app.create_app()
