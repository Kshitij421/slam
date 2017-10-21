# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


def post_view(request):
	return HttpResponse("<h1>Hello</h1>")

class HomeView(TemplateView):
	template_name = "index.html"

class display_profile():
	display = "aa"