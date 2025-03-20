from django import forms 
from django.contrib.auth.models import User
from basic_app.models import UserProfileFormInfo

class UserForm(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model= User
        fields= ('first_name','last_name','username','email','password')

class UserProfileFormInfo(forms.ModelForm):
    class Meta():
        model= UserProfileFormInfo
        fields = ('portfolio_site','profile_pic')