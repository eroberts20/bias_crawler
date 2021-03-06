# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-26 05:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biasapp', '0009_auto_20170326_0512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='negative',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='url',
            name='neutral',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='url',
            name='positive',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
    ]
