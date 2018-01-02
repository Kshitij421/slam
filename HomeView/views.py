from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response,redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
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

def signup_view(request):
	print("Inside SignUp !!!")
	if request.POST:
		username = request.POST["username"]
		email = request.POST["email"]
		password = request.POST["password"]

		Profile.objects.filter(username__exact = username)

	
	return render(request, "HomeView/index.html", context_instance=context)


def signup_view(request):
	print("Inside SignUp View !!!")
		# user = form.save(commit=False)
  #   	user.is_active = False
  #   	user.save()
  #     	current_site = get_current_site(request)
  #      	mail_subject = 'Activate your blog account.'
  #      	message = render_to_string('acc_active_email.html', {
  #               'user': user,
  #               'domain': current_site.domain,
  #               'uid':urlsafe_base64_encode(force_bytes(user.pk)),
  #               'token':account_activation_token.make_token(user),
  #           })
  #           to_email = form.cleaned_data.get('email')
  #           email = EmailMessage(
  #                       mail_subject, message, to=[to_email]
  #           )
  #           email.send()
  #           return HttpResponse('Please confirm your email address to complete the registration')


def activate_view(request):
	print(" Inside Activate View")

def login_view(request):
	print("Inside Login View")
	logout(request)
	username = password = ''
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		print (username)
		print (password)
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				print("User Autjenticated")
				return HttpResponseRedirect('/profile/'+str(user.id)+'/')
		return render_to_response('HomeView/index.html', context_instance=RequestContext(request))

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
	print("Inside logout !!!!")
	auth.logout(request)
	request.session.flush()
	username = ""
	if not request.user.is_anonymous():
		username = request.user.first_name + ' ' + request.user.last_name
	context = RequestContext(request,
						{'request': request,
                         'user': request.user,
                         'username': username})
	return HttpResponseRedirect('/')
	return render(request, "HomeView/index.html", context_instance=context)


