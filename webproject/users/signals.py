# from django.db.models.signals import post_save  # now this is a signal and get fired after a object created
# from django.contrib.auth.models import User #and it is going to be called sender and we also need to create a reciver and a reciver fn gets this signal and performs some task
# from django.dispatch import receiver   #so we import receiver
# from .models import Profile

# #we doing this because we want user profile to be created for each new user so let write a fun called create_profile

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
# 	if created:
# 		Profile.objects.create(user=instance)#so now we have create_profile fn and that we want run every time when user is created so we have not tide this funanality yet so to do this by recevier and the recevier is going to be a decoredor that we add to our function


# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
# 	instance.profile.save()


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

    instance.profile.save()