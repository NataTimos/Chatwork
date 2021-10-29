from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    posts = models.ForeignKey('Post', on_delete=models.CASCADE, default= None, null=True, blank=True)
    
    def __srt__(self):
        return self.username

class Post(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE, default= None, null=True, blank=True)
    author = models.CharField(max_length = 50, default="User")
    email = models.EmailField(max_length= 50)
    text = models.CharField(max_length = 99, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
    
    def __str__(self):
        return self.text
