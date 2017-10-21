from django.shortcuts import render
from django.http import HttpResponse
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import auth
# Create your views here.@login_required

@login_required
def logout(request):
    for sesskey in request.session.keys():
        del request.session[sesskey]
    auth.logout(request)
    return render(request, "HomeView/index.html", {})

def home_view(request):
	context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
	return render(request, "HomeView/index.html", context_instance=context)

