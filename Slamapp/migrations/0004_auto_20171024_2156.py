# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-24 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Slamapp', '0003_auto_20171024_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='facebook_profile',
            field=models.SlugField(max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='insta_profile',
            field=models.SlugField(max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_link',
            field=models.SlugField(max_length=255),
        ),
    ]