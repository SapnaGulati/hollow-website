from hollow.settings.base import *

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# For Django CI
if os.environ.get('GITHUB_WORKFLOW'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'github_actions',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': '127.0.0.1',
            'PORT': '8000',
        }
    }
