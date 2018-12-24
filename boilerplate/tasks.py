from .celery import app
from celery.utils.log import get_task_logger
from .msg import send_msg

logger = get_task_logger(__name__)

@app.task
def send_msg_task(message):
    logger.info("Sending message")
    if not send_msg(message):
        logger.warn("Failed to send message")
