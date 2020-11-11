from django.db import models

# Create your models here.
class Post(models.Model):
    first_Name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)





