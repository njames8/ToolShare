""" 
file: forms.py
language: python3
author: Nicholas James 
author: Andrew Carpenter 
description: The forms that take information throughout toolshare
"""

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.utils.translation import ugettext, ugettext_lazy as _

class LoginForm(forms.Form):
    """
    The form that appears at the login screen.
    asks for username and password
    """
    email = forms.EmailField()
    password = forms.CharField(max_length = 100, widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        # email = username
        # user = User.objects.create_user(username, email, password)
        # print(user)
        user = authenticate(username=username, password=password)
        print(user)
        if not user: # or not user.is_active:
            print("Invalid username or password.")
            raise forms.ValidationError("Sorry, that username or password was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        print("User is valid, active and authenticated")
        print(user)
        return user


class RegisterForm(UserCreationForm):
	"""
	The form that handles user registration
	asks for:
		username
		email
		first name
		last name
		password
		location
	"""
	email = forms.EmailField(label='Email', required=True)
	first_name = forms.CharField(label='First Name', required=True)
	last_name = forms.CharField(label='Last Name', required=True)
	location= forms.CharField(label="Zipcode",required=True)
	class Meta:
		model = UserProfile
		fields = ["username", "first_name", "last_name", "email", "password1", "password2", 'location']


class ToolCreateForm(forms.ModelForm):
	"""
	Form that handles tool creation
	"""
	choices = [(1, '★☆☆☆☆'), (2, '★★☆☆☆'), (3, '★★★☆☆'), (4, '★★★★☆'), (5, '★★★★★')]
	toolCondition = forms.ChoiceField(choices=choices)
	class Meta:
		model = Tool
		fields = ('name','description','availability','inShed','shed','toolCondition')

class ShedCreateForm(forms.ModelForm):
    """
    form that handles shed creation
    """
    name = forms.CharField(max_length = 50, required = True)
    location = forms.CharField(label="Zipcode", required=True, )
    class Meta:
        model = Shed
        fields = ('name', 'location',)

class EditProfileForm(forms.ModelForm):
    """
    Handles changes users make to their profile info
    """
    email = forms.EmailField(label='Email', required=True)
    first_name = forms.CharField(label='First Name', required=True)
    last_name = forms.CharField(label='Last Name', required=True)
    location = forms.CharField(label="Zipcode", required=True)
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'location']


