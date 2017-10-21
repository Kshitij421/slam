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
# from Slamapp import views as post_views
# from HomeView import views as home_views
# from Slamapp.views import HomeView
from ProfileView import views as profile_views
urlpatterns = [

#for reference
#	  url(r'^$', home_view, name='home'),
#     url(r'^contact/$', ContactView.as_view(), name='contact'),
#     url(r'^about/$', AboutView.as_view(), name='about'),
#     url(r'^profile/(?P<username>[\w.@+-]+)/$', profile_detail, name='about'),
#     url(r'^article/(?P<slug>[\w-]+)/$', article_detail, name='about'),
#     url(r'^blog/', include("blog.urls")),
#     url(r'^admin/', admin.site.urls),
#profile_create
    #url(r'^profile_create/$', post_views.post_view),
#profile_delete
    #url(r'^profile_delete/$', post_views.post_view),
#profile view
    url(r'^(?P<userid>[0-9]+)/', profile_views.get_user_profile),
#profile_edit
    #url(r'^profile_edit/$', post_views.post_view),
#check profile validity
    url(r'^select/', profile_views.select_profile),
    url(r'^', include("HomeView.urls")),
]
	