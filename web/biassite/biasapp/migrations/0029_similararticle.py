# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-25 11:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biasapp', '0028_articles_posted_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimilarArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_url', models.CharField(max_length=700)),
                ('title', models.CharField(max_length=300, null=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biasapp.Articles')),
            ],
        ),
    ]
