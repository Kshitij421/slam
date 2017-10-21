"""Slam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from Slamapp import views as post_views
from django.contrib.auth.views import logout_then_login

from . import views as home_views
urlpatterns = [

#for reference
#	  url(r'^$', home_view, name='home'),
#     url(r'^contact/$', ContactView.as_view(), name='contact'),
#     url(r'^about/$', AboutView.as_view(), name='about'),
#     url(r'^profile/(?P<username>[\w.@+-]+)/$', profile_detail, name='about'),
#     url(r'^article/(?P<slug>[\w-]+)/$', article_detail, name='about'),
#     url(r'^blog/', include("blog.urls")),
#     url(r'^admin/', admin.site.urls)
	url(r'^logout/', lambda request: logout_then_login(request, "/"), name='logout'),
	#url(r'^logout/', home_views.logout),
    url(r'^$', home_views.home_view),
]