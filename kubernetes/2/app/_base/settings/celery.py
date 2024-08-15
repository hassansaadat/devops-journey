from decouple import config

CELERY_BROKER_URL = config('CELERY_BROKER_URL')

CELERY_BEAT_SCHEDULE = {
    'test task': {
        'task': 'apps.users.tasks.test.test',
        'schedule': 60 * 1,
    }
}
