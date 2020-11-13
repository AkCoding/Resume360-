from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    first_Name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    desc = models.CharField(max_length=1000, blank=True)
    def __str__(self):
        return f'{self.user.username} Profile'



