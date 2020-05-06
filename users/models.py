from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# If a user is deleted from the database the profile picture will also be deleted
# creating an image field here and upload two creates a dictonary that the profile pic will be uploaded two the name profile pics will make a profile pic directory in the root directory


from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
        # this method is a method thats run after we save our profile pic

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     # now where going grab the saved Image an resize It
    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
