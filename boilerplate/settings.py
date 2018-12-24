"""
Main settings file

"""
import os
from celery.schedules import crontab


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.getenv('STATIC_ROOT', default='')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', default='3s3n$h-ek)gqlspc1^3^m(*$x%z=93$ibm=ck6$e49ddw^qy57')


# SECURITY WARNING: don't run with debug turned on in production!
if 'PRODUCTION' in os.environ:
    DEBUG = False
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
else:
    DEBUG = True
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False

ALLOWED_HOSTS = ['*']

# Static files
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'static', STATIC_ROOT),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_results',

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

ROOT_URLCONF = 'boilerplate.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'boilerplate.wsgi.application'

# Cache Configs
# Memcached Configs --> from memcached docs

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}


if 'MEMCACHED_HOST' in os.environ:
    CACHES['default']['LOCATION'] = os.getenv('MEMCACHED_HOST')


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

if 'DATABASE_HOST' in os.environ:
    DATABASES['default']['HOST'] = os.getenv('DATABASE_HOST')
    DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
    DATABASES['default']['NAME'] = os.getenv('DATABASE_NAME')
    DATABASES['default']['USER'] = os.getenv('DATABASE_USER')
    DATABASES['default']['PASSWORD'] = os.getenv('DATABASE_PASSWORD')


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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

# Celery Configurations
# Celery & Broker settings

CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', default="amqp://guest:guest@rabbitmq")
CELERY_RESULTS_BACKEND = os.getenv('CELERY_RESULTS_BACKEND', default="amqp://guest:guest@rabbitmq")

CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = os.getenv('CELERY_TIMEZONE', default='Europe/Rome')

# Celery cron scheduling

CELERY_BEAT_SCHEDULE = {
    # TASKS

    # 'send_task': {
    #    'task': 'emailservice.tasks.send_birthday_greeting', #function
    #   'schedule': crontab(minute='5', hour='8'), 
    #},

}

# Django celery results configurations
CELERY_RESULT_BACKEND = 'django-db'

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



