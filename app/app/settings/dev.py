import os
from .base import *

SECRET_KEY = '4ik4_4h1)3oaw#e07kj-$jcd+xr^qij31k2yasf^-(p64@oa=3'

DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('DB_HOST'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
    }
}

MEDIA_ROOT = '/vol/web/media'  # where to store all media
STATIC_ROUTE = '/vol/web/static'  # where to store all static files
