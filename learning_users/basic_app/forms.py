from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo  # Увери се, че моделът е правилно дефиниран
from phonenumber_field.formfields import PhoneNumberField  # Увери се, че django-phonenumber-field е инсталиран

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password', 'email')

class UserProfileInfoForm(forms.ModelForm):
    phone_number = PhoneNumberField(required=True)  # Добавено е phone_number
    location = forms.CharField(max_length=100, required=True,null=False)  # Градът е задължителен
    profile_pic_d = forms.ImageField(required=False)  # Снимката за D е по избор

    class Meta:
        model = UserProfileInfo
        fields = ('phone_number', 'location', 'profile_pic',)
