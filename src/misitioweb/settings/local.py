from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # Conector de DB
        'NAME': 'misitioDB',
        'USER': 'postgres',
        'PASSWORD': 'Hackerman79',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}