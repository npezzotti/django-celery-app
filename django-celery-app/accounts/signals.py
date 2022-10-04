import logging

from django.contrib.auth.signals import user_logged_in, user_login_failed, user_logged_out
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import CustomUser


logger = logging.getLogger(__name__)

@receiver(user_logged_in)
def post_login(sender, user, request, **kwargs):
    logger.info(f"Succesful login by {user.email}")

@receiver(user_login_failed)
def post_failed_login(sender, credentials, request, **kwargs):
    logger.info(f"Failed login by {credentials.get('username', '')}")

@receiver(user_logged_out)
def post_logout(sender, user, request, **kwargs):
    logger.info(f"Succesful logout by {user.email}")

@receiver(post_save, sender=CustomUser)
def post_register_user(sender, instance, created, **kwargs):
    if created:
        logger.info(f"User '{instance}' successfully registered.")

