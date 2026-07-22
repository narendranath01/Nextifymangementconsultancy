import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ==============================================================================
# ADD THIS TEMPLATES BLOCK (This resolves the TemplateDoesNotExist error)
# ==============================================================================
TEMPLATES = [
    {
        '
        "BACKEND": "django.template.backends.django.DjangoTemplates",
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

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Fix: Changed "Static" to lowercase "static" to match Linux case-sensitivity
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Required for Whitenoise to collect and serve your styles on Render
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
