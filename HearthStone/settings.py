"""
Django settings for HearthStone project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import sys
import datetime
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mr=a6w(1#h14t2e=6cm33och9vx+t16k=*c=n_b0#+#_9n*s*('

#########https
SECURE_SSL_REDIRECT = False



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']
AUTHENTICATION_BACKENDS = (#自定义用户认证
    'users.views.CustomBackend',
)
AUTH_USER_MODEL='users.UserProfile'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'xadmin',
    'cards.apps.CardsConfig',
    # 'cards'
    'users.apps.UsersConfig',
    'crispy_forms',
    'rest_framework',
    'django_filters',
    'rest_framework.authtoken',
    'corsheaders',  # 跨域使用
    'sslserver',#https
    'django_apscheduler',
]

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]


MIDDLEWARE = [  # Or MIDDLEWARE_CLASSES on Django < 1.10

    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


]

ROOT_URLCONF = 'HearthStone.urls'
CORS_ORIGIN_ALLOW_ALL = True

# CORS_ORIGIN_WHITELIST = (
#     '127.0.0.1:8080',
#     'localhost:8080',
# )
CORS_ALLOW_CREDENTIALS = True
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'HearthStone.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "hearthstone",#数据库
        'USER':"root",
        'PASSWORD':"123456",
        'HOST':"127.0.0.1",
        'OPTIONS':{
        "init_command":"SET foreign_key_checks = 0;",
        }


    },
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (

        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
         'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',  # jwt   验证
        # 'rest_framework.authentication.TokenAuthentication',
    )
}

JWT_AUTH = {

    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=30),#过期时间
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,

    'JWT_ALLOW_REFRESH': False,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=30),

    'JWT_AUTH_HEADER_PREFIX': 'JWT',
    'JWT_AUTH_COOKIE': None,

}

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'  #中文支持，django1.8以后支持；1.8以前是zh-cn
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = True   #默认是Ture，时间是utc时间，由于我们要用本地时间，所用手动修改为false！！！！


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = "/media/"
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MEDIA_ROOT = os.path.join(BASE_DIR, "media")



STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')
DATA_UPLOAD_MAX_NUMBER_FIELDS = 50000



