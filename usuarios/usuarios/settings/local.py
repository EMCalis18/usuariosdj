from .base import *

DEBUG = True

ALLOWED_HOSTS = []
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DB_NAME'),
        'USER': get_secret('USER'),
        'PASSWORD': get_secret('PASSWORD'),
        'HOST': 'localhost', 
        'PORT': '5432', 

    }
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')] #DIR = DIRECTORIO DE LOS ARCHIVOS STATIC

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')