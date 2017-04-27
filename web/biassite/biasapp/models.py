from django.db import models

from django.contrib.auth.models import User


# Create your models here

class Articles(models.Model):
    article_url = models.CharField(max_length=700)
    website = models.CharField(max_length=100)
    title = models.CharField(max_length=300, null=True)
    calc_bias = models.DecimalField(decimal_places = 5, max_digits = 10, default=0.0)
    #all_sides_bias = models.DecimalField(decimal_places = 5, max_digits = 10, default=0.0)
    social_meida_ref = models.IntegerField(default=0)
    unknown_links = models.IntegerField(default=0)
    total_links = models.IntegerField(default=1)
    self_reference = models.IntegerField(default=0)
    posted_on = models.DateTimeField(auto_now_add=True)
    edu_links =  models.IntegerField(default=0)
    gov_links =  models.IntegerField(default=0)

    #others fields...
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Url(models.Model):
    link_url =  models.CharField(max_length=700)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=True)
    text = models.CharField(max_length=10000, default=None)
    positive = models.DecimalField(decimal_places = 5, max_digits = 10, default=0.0)
    negative = models.DecimalField(decimal_places = 5, max_digits = 10, default=0.0)
    neutral = models.DecimalField(decimal_places = 5, max_digits = 10, default=0.0)

class SimilarArticle(models.Model):
    link_url =  models.CharField(max_length=700)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=True)

# Create your models here.
