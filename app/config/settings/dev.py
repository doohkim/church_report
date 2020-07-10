from .base import *

SECRETS_DEV = SECRETS_FULL['dev']

DEBUG = True

WSGI_APPLICATION = 'config.wsgi.dev.application'

# Static files (CSS, JavaScript)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ROOT_DIR, '.static')

# Media Files (Images, i.e. User Uploads)

MEDIA_ROOT = os.path.join(ROOT_DIR, '.media')
MEDIA_URL = '/media/'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

ALLOWED_HOSTS += [
    '*',
]

INSTALLED_APPS += [
    'django_extensions',
]
