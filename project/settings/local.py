"""Development settings and globals."""

from os.path import join, normpath

from base import *

########## MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('django', 'django@mercycorps.org'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
########## END MANAGER CONFIGURATION


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
########## END EMAIL CONFIGURATION

########## EMAIL SETTINGS

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'systems@mercycorps.org'
EMAIL_HOST_PASSWORD = 'MCSys2015'
DEFAULT_FROM_EMAIL = 'systems@mercycorps.org'
SERVER_EMAIL = "glind@mercycorps.org"
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#DEFAULT_TO_EMAIL = 'to email'

########## END EMAIL SETTINGS


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'helpdesk',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'helpdesk',
        'PASSWORD': 'ttmhelpdesk2015',
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

########## END DATABASE CONFIGURATION



########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
########## END CACHE CONFIGURATION


########## LOCAL DEV APPS
DEV_APPS = (
    'debug_toolbar',
)

INSTALLED_APPS = INSTALLED_APPS + DEV_APPS

########### HACKPAD
HACKPAD_CLIENT_ID = "obceRteSJqv"
HACKPAD_SECRET = "vrelEoj3WHW3bzjHiMZxX6oXfbVNAQnu"

########## GITHUB
GITHUB_AUTH_TOKEN = "ca57982c164659e0ac45f7d59a00d4914d48b895"
GITHUB_REPO = "https://api.github.com/repos/mercycorps/tola-help/issues"

########## GOOGLE AUTH
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "445847194486-gl2v6ud6ll65vf06vbjaslqqgejad61k.apps.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "qAAdNMQy77Vwqgj4YgOu20f7"
