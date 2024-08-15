from celery import shared_task
import logging

logger = logging.getLogger(__name__)


@shared_task
def test():
    logger.error(msg="Test Periodic Task")
