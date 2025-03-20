from django import forms
from django.contrib.auth.models import UserD,UserP
from basic_app.models import UserProfileInfo

class UserFormP(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = UserP
        fields = ('first_name','last_name','telephone','username','password')

class UserFormD(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model= UserD
        fields= ('first_name','last_name','telephone','email','username','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic',)
