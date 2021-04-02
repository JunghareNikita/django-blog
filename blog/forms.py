from django import forms
from django.forms import ModelForm
from .models import BlogsModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BlogForm(ModelForm):
  class Meta:
      model = BlogsModel
      fields = '__all__'

class SignupForm(UserCreationForm):
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput)
    username = forms.CharField(max_length=100, widget=forms.TextInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email'}



