"""
Django settings for BMS project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-zx)%8$+lf8_&i+8a^w2qq1+hvc7x_*j_=n5%%r%flwsqcu#p!v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
X_FRAME_OPTIONS = 'SAMEORIGIN'

# Application definition

INSTALLED_APPS = [
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'Admin',
    'HR',
    'AMG',
    'BDG',
    'CCG',
    'CorPlan',
    'IAD',
    'Legal',
    'OGM',
    'SPG',
]

JET_THEMES = [
    {
        'theme': 'default', # theme folder name
        'color': '#47bac1', # color of the theme's button in user menu
        'title': 'Default' # theme title
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]

JET_SIDE_MENU_ITEMS = [
    {
        'label': 'Monitoring',
        'items': [
            {'name': 'core.budget'},
            {'name': 'core.funds'},
            {'name': 'core.mooe'},

        ]
    },
    {
        'label': 'HR Budget',
        'items': [
            {'name': 'HR.annual'},
            {'name': 'HR.quarter'},

        ]
    },
       {
        'label': 'Admin Budget',
        'items': [
            {'name': 'Admin.annual'},
            {'name': 'Admin.quarter'},

        ]
    },
    {
        'label': 'AMG Budget',
        'items': [
            {'name': 'AMG.annual'},
            {'name': 'AMG.quarter'},

        ]
    },
    {
        'label': 'BDG Budget',
        'items': [
            {'name': 'BDG.annual'},
            {'name': 'BDG.quarter'},

        ]
    },
    {
        'label': 'CCG Budget',
        'items': [
            {'name': 'CCG.annual'},
            {'name': 'CCG.quarter'},

        ]
    },
    {
        'label': 'CorPlan Budget',
        'items': [
            {'name': 'CorPlan.annual'},
            {'name': 'CorPlan.quarter'},

        ]
    },
    {
        'label': 'IAD Budget',
        'items': [
            {'name': 'IAD.annual'},
            {'name': 'IAD.quarter'},

        ]
    },
    {
        'label': 'Legal Budget',
        'items': [
            {'name': 'Legal.annual'},
            {'name': 'Legal.quarter'},

        ]
    },
    {
        'label': 'OGM Budget',
        'items': [
            {'name': 'OGM.annual'},
            {'name': 'OGM.quarter'},

        ]
    },
    {
        'label': 'Dropdown Database',
        'items': [
            {'name': 'core.workgroup'},
            {'name': 'core.reference'},
            {'name': 'core.account_code'},
            {'name': 'core.account_name'},
            {'name': 'core.payee'},
            {'name': 'core.budget_category'},
            {'name': 'core.sources_classification'},
        ]
    },



]
JET_CHANGE_FORM_SIBLING_LINKS = True
# ... existing code ...

# ... existing code ...
JET_INDEX_DASHBOARD = 'jet.dashboard.dashboard.DefaultIndexDashboard'
JET_APP_INDEX_DASHBOARD = 'jet.dashboard.dashboard.DefaultAppIndexDashboard'



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'BMS.urls'

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

WSGI_APPLICATION = 'BMS.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'