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

########### HACKPAD
HACKPAD_CLIENT_ID = "obceRteSJqv"
HACKPAD_SECRET = "vrelEoj3WHW3bzjHiMZxX6oXfbVNAQnu"

########## GITHUB
GITHUB_AUTH_TOKEN = "2685bac2fe078dd3b276f94ccc301a13b0656a80"
GITHUB_REPO_1 = "https://api.github.com/repos/mercycorps/tola"
GITHUB_REPO_2 = "https://api.github.com/repos/mercycorps/tola-activity"

########## GOOGLE AUTH
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "445847194486-gl2v6ud6ll65vf06vbjaslqqgejad61k.apps.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "qAAdNMQy77Vwqgj4YgOu20f7"

########## LOCAL DEV APPS
DEV_APPS = (
    'debug_toolbar',
)

INSTALLED_APPS = INSTALLED_APPS + DEV_APPS