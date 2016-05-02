from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from my_user_profile_app.models import UserDetails

@receiver(post_save, sender=User)
def handle_user_save(sender, instance, created, **kwargs):
  if created:
    UserDetails.objects.create(user=instance)