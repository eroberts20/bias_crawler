from django.db import models

from django.contrib.auth.models import User

# Create your models here

class Articles(models.Model):
    article_url = models.CharField(max_length=300)
    title = models.CharField(max_length=300, null=True)

    #others fields...
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Url(models.Model):
    link_url =  models.CharField(max_length=301)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=True)
