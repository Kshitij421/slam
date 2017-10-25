# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import os
from uuid import uuid4
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils.deconstruct import deconstructible

@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)

get_profile_photo_path = PathAndRename("profile_photoes")
get_post_photo_path = PathAndRename("posts")

class Profile(models.Model):
	GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
	user = models.ForeignKey(User)
	username = models.CharField(max_length=15)
	gender = models.CharField(max_length=1, default='M', choices=GENDER_CHOICES)
	email = models.EmailField(primary_key=True)
	profile_link = models.SlugField(unique=False, max_length=255)
	profile_image = models.ImageField(upload_to=get_profile_photo_path, blank=True, null=True)
	birth_date = models.DateTimeField(null=True, blank=True)
	insta_profile = models.SlugField(unique=False, max_length=255)
	facebook_profile = models.SlugField(unique=False, max_length=255)


class Post(models.Model):
	profile = models.ForeignKey(Profile)
	title = models.CharField(max_length=255)
	email = models.EmailField()
	slug = models.SlugField(unique=True, max_length=255, primary_key=True)
	post_feed = models.ImageField(upload_to=get_post_photo_path, blank=True, null=True)
	content = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	author = models.TextField()

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title