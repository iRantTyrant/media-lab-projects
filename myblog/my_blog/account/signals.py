from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

# Signal to create or update the Profile when a User is saved
@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        # Create a Profile when the User is created
        Profile.objects.create(user=instance)
    else:
        # Update the Profile when the User is updated
        instance.profile.save()
# This signal ensures that a Profile is always created or updated when a User is saved.