# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 02:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biasapp', '0005_articles_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='links',
            field=models.ManyToManyField(blank=True, related_name='_articles_links_+', to='biasapp.Articles'),
        ),
    ]
