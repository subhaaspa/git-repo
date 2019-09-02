from django import forms
from users_apps.models import UserProfileInfo
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('profile_URL','profile_image')
