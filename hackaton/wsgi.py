"""
WSGI config for hackaton project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hackaton.settings')
os.environ.setdefault('DEBUG', 'FALSE')
os.environ.setdefault('ALLOWED_HOSTS', 'ghettoddos.pythonanywhere.com')
os.environ.setdefault('SECRET_KEY', 'django-insecure-0!*c32(h(=4&xxk^y#@9(=j2ddvvgq-bo%z8x04gvd*vkef)2_')

application = get_wsgi_application()
