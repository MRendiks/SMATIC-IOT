"""
WSGI config for apismatic project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import threading
from django.core.wsgi import get_wsgi_application
from apismatic.mqtt.client import client

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apismatic.settings')

threading.Thread(target=client.loop_forever).start()

application = get_wsgi_application()
