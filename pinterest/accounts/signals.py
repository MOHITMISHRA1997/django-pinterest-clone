from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile,MyBaseUser


@receiver(post_save,sender=MyBaseUser)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save,sender=MyBaseUser)
def post_save(sender,instance,**kwargs):
    instance.profile.save()


