import logging
import os
from smtplib import SMTPException
from time import sleep

from celery import shared_task
from django.core.mail import send_mail

logger = logging.getLogger(__name__)


@shared_task(name='send_welcome_email')
def send_welcome_email_task(username, email):
    """Sends a welcome email to a user when they sign up."""
    logger.info(f"Processing welcome email for {email}")
    sleep(5)  # Simulate an operation that takes some time to run
    try:
        send_mail(
            f"Welcome {username}!",
            f"Hi {username},\n\nThank you for signing up for our site!\nThis email was sent by a celery worker with process ID {os.getpid()}.\n",
            "noreply@example.com",
            [email],
            fail_silently=False,
        )
        logger.info(f"Welcome email successfully sent to {email}")
    except SMTPException:
        logger.error(f"Failed to send welcome email to {email}")

