"""
Django settings for edcred project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-828^sbusw-yvqa3xya$pd6)=^f$n1#5db%bdwanxd29)is*jtz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '*'
]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',  # Replace with the URL of your ReactJS client
    'http://127.0.0.1:3000',  # If using localhost with IP address
    'https://f2b0-2401-4900-61c6-f7d4-c4ab-c401-7f76-1dfb.ngrok-free.app',# Replace with your ngrok URL
]
CORS_ORIGIN_ALLOW_ALL = False
# Application definition


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    "django_extensions",
    #User defined apps    
    'events.apps.EventsConfig',
    'home.apps.HomeConfig',
    'project.apps.ProjectConfig',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'edcred.urls'

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

WSGI_APPLICATION = 'edcred.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# CROSS ORIGIN REQUEST SETTINGS

CORS_ORIGIN_WHITELIST = [ 
    'http://localhost:3000',  # Replace with the URL of your ReactJS client
    'http://127.0.0.1:3000',  # If using localhost with IP address
    'https://f2b0-2401-4900-61c6-f7d4-c4ab-c401-7f76-1dfb.ngrok-free.app',# Replace with your ngrok URL
]

CORS_ALLOW_HEADERS = [
    'Accept',
    'Accept-Encoding',
    'Authorization',
    'Content-Type',
    'Cookie',  # Add 'Cookie' header to allow
    'Origin',
    'Access-Control-Request-Method',
    'Access-Control-Request-Headers'
]

CORS_ALLOWED_METHODS = [
    'GET',
    'POST',
    'OPTIONS',
    # Add other allowed methods as needed
]


CORS_ALLOW_CREDENTIALS = True

SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = "None"
SESSION_COOKIE_PATH = '/'
SESSION_COOKIE_DOMAIN = "None"



# CSRF_TRUSTED_ORIGINS = [
#     'http://*',
#     'https://*' 
# ]

# CSRF_COOKIE_HTTPONLY = False
# CSRF_COOKIE_SAMESITE = None
# CSRF_COOKIE_DOMAIN = None






