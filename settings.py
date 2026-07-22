# Django settings for Nextify project.
# This is a test comment for Git

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "Static"),
]

DEBUG = True  # Enable debug mode for development
# Other existing settings...


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
            os.path.join(BASE_DIR, 'templates'),
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


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # Ensure this path is correct
    }
}

# 1. Ensure WhiteNoise is right under SecurityMiddleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # <-- Make sure this is here!
    'django.contrib.sessions.middleware.SessionMiddleware',
    ...
]

# 2. Add this at the bottom of settings.py for caching static assets
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
