"""Common settings and globals."""
import os

#  PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:
CONFIG_ROOT = os.path.dirname(os.path.dirname(__file__))
DJANGO_ROOT = os.path.dirname(CONFIG_ROOT)

PROJECT_ROOT = os.path.dirname(DJANGO_ROOT)

SITE_NAME = os.path.basename(DJANGO_ROOT)

# SECRET CONFIGURATION
# Note: This key should only be used for development and testing.
SECRET_KEY = "$3nr$oe@bfzz(if6si$!n$!#u54nfd^ak_i255ryz5run139d4"

# DEBUG CONFIGURATION
DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = []

# MANAGER CONFIGURATION
ADMINS = (
    ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS

# GENERAL CONFIGURATION
TIME_ZONE = 'Pacific/Auckland'
USE_TZ = True

LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True

SITE_ID = 1
WSGI_APPLICATION = '{}.wsgi.application'.format(SITE_NAME)

# URL CONFIGURATION
ROOT_URLCONF = '{}.urls'.format(SITE_NAME)
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

# MEDIA CONFIGURATION
MEDIA_ROOT = os.path.join(DJANGO_ROOT, 'media')
MEDIA_URL = '/media/'

# STATIC FILE CONFIGURATION
STATIC_ROOT = os.path.join(DJANGO_ROOT, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(CONFIG_ROOT, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# TEMPLATE CONFIGURATION
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(DJANGO_ROOT, 'templates'),
)

# MIDDLEWARE CONFIGURATION
MIDDLEWARE_CLASSES = (
    # Default Django middleware.
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# APP CONFIGURATION
DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

THIRD_PARTY_APPS = ()

LOCAL_APPS = (
    'common',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
