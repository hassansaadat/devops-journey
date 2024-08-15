# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

from decouple import config

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT"),
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "TEST": {
            "NAME": "test_db",
        },
    }
}
