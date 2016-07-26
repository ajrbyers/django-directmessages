__version__ = '0.9.2'

try:
    from django import VERSION as DJANGO_VERSION
    if DJANGO_VERSION >= (1, 7):
        default_app_config = 'directmessages.apps.DirectmessagesConfig'
except ImportError:
    pass
