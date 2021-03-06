"""
Django settings for fc_django project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ad$obz5a*-7ruylafb#+x^$&8a8)i-(-9m64j@4rjodiw&^-cl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

BATON = {
    'SITE_HEADER': '패스트캠퍼스 백오피스',
    'SITE_TITLE': '패스트캠퍼스 백오피스',
    'INDEX_TITLE': '패스트캠퍼스 관리자페이지',
    'SUPPORT_HREF': 'https://fastcampus.co.kr',
    'COPYRIGHT': 'copyright © 2020 Fastcampus',
    'POWERED_BY': '<a href="https://fastcampus.co.kr">Fastcampus</a>',
    'MENU_TITLE': '패스트캠퍼스',
    'MENU': (
        { 'type': 'title', 'label': 'main' },
        {
            'type': 'app',
            'name': 'fcuser',
            'label': '사용자',
            'icon': 'fa fa-lock',
            'models': (
                {
                    'name': 'fcuser',
                    'label': '사용자'
                },
            )
        },
        {
            'type': 'free', 'label': '주문', 'default_open': True, 'children': [
                { 'type': 'free', 'label': '주문', 'url': '/admin/order/order/' },
                { 'type': 'free', 'label': '주문 날짜 뷰', 'url': '/admin/order/order/date_view/' },
            ]
        },
        {
            'type': 'app',
            'name': 'product',
            'label': '상품',
            'models': (
                {
                    'name': 'product',
                    'label': '상품'
                },
            )
        },
        { 'type': 'free', 'label': '매뉴얼', 'url': '/admin/manual' },
    ),
}

INSTALLED_APPS = [
    'baton',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'rest_framework',
    'fcuser.apps.FcuserConfig',
    'order.apps.OrderConfig',
    'product.apps.ProductConfig',

    'baton.autodiscover'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fc_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'fc_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
