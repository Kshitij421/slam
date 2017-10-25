
from social.backends.google import GoogleOAuth2
from social.backends.twitter import TwitterOAuth
from social.backends.facebook import FacebookOAuth2
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from django.contrib import auth
from Slamapp.models import Profile


def socialprofile_extra_values(backend, details, response, uid, user, *args, **kwargs):
    """Routes the extra values call to the appropriate back end"""
    if type(backend) is GoogleOAuth2:
        google_extra_values(backend, details, response, uid, user, *args, **kwargs)

    if type(backend) is TwitterOAuth:
        twitter_extra_values(backend, details, response, uid, user, *args, **kwargs)

    if type(backend) is FacebookOAuth2:
        facebook_extra_values(backend, details, response, uid, user, *args, **kwargs)


def google_extra_values(backend, details, response, uid, user, *args, **kwargs):
    """Populates a UserProfile Object when a new User is created via Google Auth"""
    if True:
    #if not profile.manually_edited:
        user.last_name = response.get('name').get('familyName', '')
        user.first_name = response.get('name').get('givenName', '')
        user.username = user.email
        user.save()

        profile = Profile()
        profile.user = user
        profile.username = response.get('name').get('givenName', '')
        profile.email = user.email
        profile.gender = response.get('gender', '')
        print("Birthday: %s"%response.get('birthday', ''))
        if response.get('birthday', ''):
            profile.birth_date = response.get('birthday', '')
        profile.profile_image = response.get('image').get('url', '')
        profile.profile_link = slugify(response.get('image').get('url', '') + str(user.id))
        profile.insta_profile = slugify(response.get('image').get('url', '') + str(user.id))
        profile.facebook_profile = slugify(response.get('image').get('url', '') + str(user.id))
        #profile.url = response.get('url', '')
        #profile.description = response.get('occupation', '')

        profile.save()

        username = user.username
        password = user.password
        kwargs = {'username': username, 'password': 'princeton335'}
        user = auth.authenticate(**kwargs)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('HomeView/index.html')
        else:
            return HttpResponseRedirect('/accounts/invalid')



def facebook_extra_values(backend, details, response, uid, user, *args, **kwargs):
    """Populates a UserProfile Object when a new User is created via Facebook Auth"""
    profile = user.social_profile
    if not profile.manually_edited:
        user.last_name = response.get('last_name', '')
        user.first_name = response.get('first_name', '')
        user.save()

        profile.gender = response.get('gender', '')
        profile.url = response.get('link', '')
        if response.get('picture', False):
            profile.image_url = response.get('picture').get('data').get('url', '')

        profile.save()

    return response


def twitter_extra_values(backend, details, response, uid, user, *args, **kwargs):
    profile = user.social_profile
    if not profile.manually_edited:
        try:
            first_name, last_name = response.get('name', '').split(' ', 1)
        except:
            first_name = response.get('name', '')
            last_name = ''
        user.last_name = last_name
        user.first_name = first_name
        user.save()

        profile.url = response.get('url', '')
        profile.image_url = response.get('profile_image_url_https', '')
        profile.description = response.get('description', '')

        profile.save()

    return response
# def get_avatar(backend, strategy, details, response,
#         user=None, *args, **kwargs):
#     url = None
#     if backend.name == 'facebook':
#         url = "http://graph.facebook.com/%s/picture?type=large"%response['id']
#     if backend.name == 'twitter':
#         url = response.get('profile_image_url', '').replace('_normal','')
#     if backend.name == 'google-oauth2':
#         url = response['image'].get('url')
#         ext = url.split('.')[-1]
#     if url:
#         user.avatar = url
#         user.save()