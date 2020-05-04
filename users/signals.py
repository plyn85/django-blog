# this page creates a profile for each new user
#  this is a signal that gets fired after an object is saved
from django.db.models.signals import post_save
# the user model is going be whats sending the signal
from django.contrib.auth.models import User
# a reciver is going to be a function the gets the signal
from django.dispatch import receiver
# importing profile from our models as we be creating a profile in our function
from .models import Profile
#  we want this function to run ever time a user is created
# this is saying that when a user is saved send the post_save signal which is sent by the reciver the reciver is create profile function which takes all the agruments that the post save signal passed to it one of those is the instance of the user and one is created
@receiver(post_save,sender=User)
def create_profile(sender, instance, created, **kwags):
    if created:
        Profile.objects.create(user=instance)
# kwargs accepts any addintional key word agrument
# saveing the users profile here
@receiver(post_save,sender=User)
def save_profile(sender, instance, **kwags):
    instance.profile.save()
