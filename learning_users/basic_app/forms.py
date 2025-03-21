from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo  
from phonenumber_field.formfields import PhoneNumberField  
from basic_app.validators import custom_pass_validation
from basic_app.validators import validate_phone_number

class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        validators=[custom_pass_validation]
                               )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password', 'email')

class UserProfileInfoForm(forms.ModelForm):
    phone_number = PhoneNumberField(required=True, initial='+359', validators=[validate_phone_number])  
    location = forms.CharField(max_length=100, required=True)
    profile_pic = forms.ImageField(required=False)
    user_type = forms.ChoiceField(choices=UserProfileInfo.USER_TYPES, required=True)  # 👈

    class Meta:
        model = UserProfileInfo
        fields = ('phone_number', 'location', 'profile_pic', 'user_type')

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if UserProfileInfo.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("Този телефонен номер вече съществува!")
        return phone_number

    def clean(self):
        cleaned_data = super().clean()
        user_type = cleaned_data.get('user_type')
        profile_pic = cleaned_data.get('profile_pic')

        if user_type == 'volunteer' and not profile_pic:
            self.add_error('profile_pic', 'Доброволците трябва да качат профилна снимка.')
        return cleaned_data
