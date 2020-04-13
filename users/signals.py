from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# Sender is the user and post_save is the signal. When a user is saved send this signal: post_save to be received by receiver which is this: create_profile.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        # If the user is created, make this profile object with the user equal to the instance of which it is created.
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()