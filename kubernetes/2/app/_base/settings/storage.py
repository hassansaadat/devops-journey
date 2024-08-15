from decouple import config


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = config('STATIC_URL')
STATIC_ROOT = config('STATIC_ROOT')
STATICFILES_DIRS = [
    'static'
]
