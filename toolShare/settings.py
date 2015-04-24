"""
Django settings for toolShare project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.core.urlresolvers import reverse_lazy

LOGIN_URL = reverse_lazy('')
LOGIN_REDIRECT_URL = reverse_lazy('home')


BASE_DIR = os.path.dirname(os.path.dirname(__file__))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(bmj=n#!o=($d)8c+dnd2@ize9qy_eamw=o#+7gn%z6^w5ns72'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True
TEMPLATE_DIRS = (
  #'C:/Users/nxj2348/Downloads/SE 261/toolShare/users',
  'users',
  'users/templates',
  'postman/templates',
  'postman/templates/postman',
  #'postman/templates/admin/postman/pendingmessage',
  'postman/templates',

)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
	'django.contrib.sessions',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'users',
    'postman',

	
)
AUTH_PROFILE_MODULE = 'users.UserProfile'
AUTHENTICATION_BACKENDS = (
	'django.contrib.auth.backends.ModelBackend',
)

SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'toolShare.urls'

WSGI_APPLICATION = 'toolShare.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },

    'users': {
    	'ENGINE':'django.db.backends.sqlite3',
    	'NAME': 'Users'
    },

    'tools': {
        'ENGINE':'django.db.backends.sqlite3',
        'NAME':'Tools'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Eastern'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
PROJECT_DIR=os.path.dirname(__file__)
STATICFILES_DIRS = ( os.path.join(PROJECT_DIR,'static/'),)
STATIC_ROOT = ''
STATIC_URL = '/static/'

POSTMAN_AUTO_MODERATE_AS = True
POSTMAN_DISABLE_USER_EMAILING = True
POSTMAN_DISALLOW_ANONYMOUS = True