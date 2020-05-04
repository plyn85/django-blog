from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# each class is a diifernet table in the data base and each attribute a differnet field in the data base
#line 4  links this table with user table on_delete tells django if a user is deleted to delete there posts
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
# this will allow a post to be printed out by the title dundared method allows you to recreate title object
    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     # this returns the path to any pecific instance
    #     # this will return the url as a string from the post detail url path the veiw then handels the rediret for us each post will be direct to its own page
    #     return reverse('post-detail',kwargs={'pk': self.pk})    

           
  



 