from decouple import config


CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': config('REDIS_URL'),
        'TIMEOUT': None,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PASSWORD': config('REDIS_PASSWORD'),
            "SOCKET_CONNECT_TIMEOUT": 60,
            "SOCKET_TIMEOUT": 60,
        },
    },
}
