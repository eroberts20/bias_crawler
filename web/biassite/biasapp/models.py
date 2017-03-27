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
    text = models.CharField(max_length=1000, default=None)
    positive = models.DecimalField(decimal_places = 5, max_digits = 10, default=0.0)
    negative = models.DecimalField(decimal_places = 5, max_digits = 10, default=0.0)
    neutral = models.DecimalField(decimal_places = 5, max_digits = 10, default=0.0)


# Create your models here.
