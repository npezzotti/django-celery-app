import os
from time import sleep

from celery import shared_task
from django.core.mail import send_mail


@shared_task(name='send_welcome_email')
def send_welcome_email_task(username, email):
    """Sends a welcome email to a user when they sign up."""
    sleep(5)  # Simulate an operation that takes some time to run
    send_mail(
        f"Welcome {username}!",
        f"Hi {username},\n\nThank you for signing up for our site!\nThis email was sent by a celery worker with process ID {os.getpid()}.\n",
        "noreply@example.com",
        [email],
        fail_silently=False,
    )
