from .base import *

ALLOWED_HOSTS = ['localhost','127.0.0.1']

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'db.sqlite3',
  }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'localhost:11211',
    }
}