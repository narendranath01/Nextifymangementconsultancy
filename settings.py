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
        # Change 'templates' here to match whatever your folder is named exactly
        'DIRS': [BASE_DIR / 'templates'], 
        'APP_DIRS': True,
        ...
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # Ensure this path is correct
    }
}
