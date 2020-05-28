from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
<<<<<<< HEAD
    instance.profile.save()
=======
    instance.profile.save()
>>>>>>> 7a3f3b372e6c30bfb5be3feb2c735d3de519caf8
