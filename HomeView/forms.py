from django import forms

class LoginForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(widget = forms.PasswordInput())


class SignupForm(forms.Form):
	username = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField(widget = forms.PasswordInput())
	confirm_password = forms.CharField(widget = forms.PasswordInput())s
