# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post
from .models import Profile

# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
	list_display= ["email", "content", "created_on"]
	list_display_link = []
	list_filter = []
	class Meta:
		model = Post

class ProfileModelAdmin(admin.ModelAdmin):
	list_display= ["username","email","birth_date"]
	list_display_link = []
	list_filter = []
	class Meta:
		model = Profile

admin.site.register(Post, PostModelAdmin)
admin.site.register(Profile, ProfileModelAdmin)