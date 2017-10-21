
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
import urllib
from django.conf import settings
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf


# Create your views here.

def get_authorization_url(request):

        # URL to where we will redirect to
        redirect_url = urllib.quote_plus(settings.SITE_URL + reverse('register_google'))

        # create a unique state value for CSRF validation
        request.session['google_state'] = unicode(csrf(request)['csrf_token'])

        scope = urllib.quote_plus('https://www.googleapis.com/auth/userinfo.email') + '+' + \
                urllib.quote_plus('https://www.googleapis.com/auth/userinfo.profile')

        # redirect to google for approval
        url = 'https://accounts.google.com/o/oauth2/auth?' \
              + 'scope=' + scope \
              + '&state=' + request.session['google_state'] \
              + '&redirect_uri=' + redirect_url \
              + '&response_type=code' \
              + '&client_id=' + settings.GOOGLE_OAUTH2_CLIENT_ID \
              + '&access_type=offline' \
              + '&approval_prompt=auto'

        return url
def verify(request):
        # Google will direct with state and code in the URL
        # ?state=zNHRjuYO...&code=4/zK5F93g2we...

        # ensure we have a session state and the state value is the same as what google returned
        if 'google_state' not in request.session \
           or 'state' not in request.GET \
           or 'code' not in request.GET \
           or request.session['google_state'] != request.GET['state']:
            return False
        else:
            return True



def get_user_profile(request, userid):
    user = User.objects.get(id=userid)
    return render(request, 'ProfileView/profile.html', {"user":user})

def select_profile(request):
	get_authorization_url(request)
	HttpResponseRedirect(url)