from django.db import models

from django.contrib.auth.models import User

# Create your models here

class Articles(models.Model):
    url = models.CharField(max_length=300)
    #others fields...
    user = models.ForeignKey(User, on_delete=models.CASCADE)
