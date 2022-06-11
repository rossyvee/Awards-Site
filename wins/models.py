from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = CloudinaryField('images')
    bio = models.TextField(max_length=500, default="This is my story,this is my life,it has been intresting", blank=True)
    name = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=60, blank=True)
    contact = models.EmailField

    def __str__(self):
        return f'{self.user.username} Profile'
