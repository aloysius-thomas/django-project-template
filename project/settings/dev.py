from project.settings.base import *

DEBUG = True
ALLOWED_HOSTS = ['*']

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "static-root"
MEDIA_ROOT = BASE_DIR / "media"
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = BASE_DIR / 'utils/email-messages/'
