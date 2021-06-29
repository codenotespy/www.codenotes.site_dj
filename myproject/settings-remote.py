"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import django_heroku
import os

# For Translate:
from django.utils.translation import ugettext_lazy as _


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l(x#6h6uefhff7%)e-wi@7kol9ajcxz0x8r%$whizz2da7&)4$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'blogapp',
    'register',
    'storages',
# Rich Text Editor
    'ckeditor',
# Rich Text Editor Upload Image Module
    'ckeditor_uploader',
    'modeltranslation',
    'taggit',
]
# 'storages' must be added as above for AWS.
# "storages.py" file should be created in project folder.


TAGGIT_CASE_INSENSITIVE = True




MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


# --- FOR DEFAULT SQLITE3 DATABASE: ---
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}



# --- FOR HEROKU POSTGRES DB: ---
#import dj_database_url
#db_from_env = dj_database_url.config(conn_max_age=600)
#DATABASES['default'].update(db_from_env)



# --- FOR LOCAL POSTGRES DB: ---
# pip install psycopg2
#DATABASES = {
#    'default':{
#       'ENGINE':'django.db.backends.postgresql_psycopg2',
#       'NAME':'blogdb',
#       'USER':'postgres',
#       'PASSWORD':'yolo1212',
#       'HOST':'localhost',
#       'PORT':'5432',
#      'ATOMATIC_REQUESTS':True,
#    }
#}

DATABASES = {
    'default':{
       'ENGINE':'django.db.backends.postgresql_psycopg2',
       'NAME':'d4ibkbem03d0m',
       'USER':'vuwkrieyjphlrt',
       'PASSWORD':'137d3cf22bea9694c36f4eb2eeaae5082cc2358858c2671587c60129fdb5d410',
       'HOST':'ec2-52-19-96-181.eu-west-1.compute.amazonaws.com',
       'PORT':'5432',
      'ATOMATIC_REQUESTS':True,
    }
}

# postgres://vuwkrieyjphlrt:137d3cf22bea9694c36f4eb2eeaae5082cc2358858c2671587c60129fdb5d410@ec2-52-19-96-181.eu-west-1.compute.amazonaws.com:5432/d4ibkbem03d0m
# postgres://YourUserName:YourPassword@YourHostname:5432/YourDatabaseName
# heroku login
# heroku update
# heroku pg:psql -a uamaster

# psql --host=ec2-54-155-226-153.eu-west-1.compute.amazonaws.com --port=5432 --username=rzoduaowqygsag --password --dbname=dfma26o0iab9fr
# ec0bca01f23fc8d0a8f5219c6423b277f26a16cc0d85880bfeb32bce963ac827

'''
# --- FOR REMOTE MYSQL: ---
# After the migration run altertables.py to make utf8 valid in the remote mysql db.
# pip install mysqlclient

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Qyn5Svq6sS',
		'USER': 'Qyn5Svq6sS',
		'PASSWORD': 'RkuHC8OuDe',
		'HOST': 'remotemysql.com',
		'PORT': '3306',
        'OPTIONS' : {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"}
    }
}
'''

# from django.db.backends.mysql.base import DatabaseWrapper
# DatabaseWrapper.data_types['DateTimeField'] = 'datetime'
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'mydb',
#		'USER': 'root',
#		'PASSWORD': '',
#		'HOST': 'localhost',
#		'PORT': '3306',
#        'OPTIONS' : {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"}
#    }
#}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

#LANGUAGE_CODE = 'en-us'
#LANGUAGE_CODE = 'tr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


LANGUAGES = [
    ('en', _('English')),
#    ('uk', _('Ukrainian')),
#    ('ar', _('Arabic')),
#    ('ja', _('Japanese')),
    ('tr', _('Turkish')),
#    ('ru', _('Russian')),
]

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

MODELTRANSLATION_FALLBACK_LANGUAGES = ('en', 'tr')



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


# Disable below to use static files from AWS S3
#STATIC_URL = '/static/'

CRISPY_TEMPLATE_PACK="bootstrap4"

LOGIN_REDIRECT_URL = "afterlogin"
LOGOUT_REDIRECT_URL = "afterlogout"

# Disable below to use static files from AWS S3
#STATIC_ROOT = os.path.join(BASE_DIR, '')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'blogapp/static')
]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'codenotes.py@gmail.com'
#EMAIL_HOST_PASSWORD = 'njefksdsoascimmo'
EMAIL_HOST_PASSWORD = 'sameuysvpzomwrpb'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'






####################################
    ##  CKEDITOR CONFIGURATION ##
####################################

# Rich Text Editor ckeditor Configuration
CKEDITOR_CONFIGS = {
    'default': {
	#Toolbar features
        'toolbar': 'full',
	#Editor Height
        'height': 300,
	# editor width
        'width': 1000,
    },
}

#CKEDITOR_CONFIGS = {
#    'default': {
#        'toolbar': None,
#    },
#}

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

# Image ckeditor file upload path, here use seven cattle cloud storage, do not fill
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"





# --- FOR AWS ---

AWS_ACCESS_KEY_ID = 'AKIAZQD2CLURHVCNNB3L'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'codenote'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
AWS_DEFAULT_ACL = 'public-read'

# Aktivate below to use static files from AWS S3
AWS_LOCATION = 'static'
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Aktivate below to use media files from AWS S3
DEFAULT_FILE_STORAGE = 'myproject.storages.MediaStore'




# Activate if you want to use your current/local sqlite3 database and current/local staticfiles in heroku
# If you activate this, you can not use remote mysql because it make you use sqlite3
#django_heroku.settings(locals())

