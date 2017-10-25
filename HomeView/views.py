from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.core.urlresolvers import reverse
from Slamapp.models import Profile
# Create your views here.@login_required

@login_required
def logout(request):
    for sesskey in request.session.keys():
        del request.session[sesskey]
    auth.logout(request)
    return render(request, "HomeView/index.html", {})

def home_view(request):
	# if request.user is not None:
	# 	if Profile.objects.filter(email__exact = request.user.username) is not None:
	# 		username = Profile.objects.filter(email__exact = request.user.username)[0].username
	username = ""
	print("user")
	print(request.user)
	if not request.user.is_anonymous():
		username = request.user.first_name + ' ' + request.user.last_name
	context = RequestContext(request,
                           {'request': request,
                            'user': request.user,
                            'username': username})

	return render(request, "HomeView/index.html", context_instance=context)

def logout_view(request):
	auth.logout(request)
	request.session.flush()
	username = ""
	if not request.user.is_anonymous():
		username = request.user.first_name + ' ' + request.user.last_name
	context = RequestContext(request,
						{'request': request,
                         'user': request.user,
                         'username': username})

	return render(request, "HomeView/index.html", context_instance=context)
