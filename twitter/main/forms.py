from django import forms
from main.models import UserProfile, Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreateForm(UserCreationForm):
    username = forms.CharField(label=(u'User Name'))
    email = forms.EmailField(label=(u'Email Address'))

    class Meta:
        model = UserProfile
        exclude = ('user','password',)


class LoginForm(forms.Form):
    username = forms.CharField(label=(u'User Name'))
    password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        exclude = ('owner',)
