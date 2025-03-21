from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo  
from phonenumber_field.formfields import PhoneNumberField  
from basic_app.validators import custom_pass_validation
from basic_app.validators import validate_phone_number

class UserForm(forms.ModelForm):
    password = forms.CharField(
        label="Парола",
        widget=forms.PasswordInput(),
        validators=[custom_pass_validation],
        error_messages={
        'required':'Моля, въведете паролата наново! '
        }  )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password', 'email')
        labels = {
            'first_name': 'Име',
            'last_name': 'Фамилия',
            'username': 'Потребителско име',
            'email': 'Имейл',
        }
        error_messages = {
            'username': {
                'required': 'Моля, въведете потребителско име.',
                'unique': 'Това потребителско име вече съществува.',
            },
            'email': {
                'required': 'Моля, въведете имейл адрес.',
                'invalid': 'Невалиден имейл адрес.',
            }
        }

class UserProfileInfoForm(forms.ModelForm):
    phone_number = PhoneNumberField(
        required=True,
        initial='+359',
        label='Телефонен номер',
        validators=[validate_phone_number],
        error_messages={
            'required': 'Моля, въведете телефонен номер.',
            'invalid': 'Моля, въведете валиден телефонен номер.'
        }
    )
    
    location = forms.CharField(
        max_length=100,
        required=True,
        label='Местоживеене',
        error_messages={
            'required': 'Моля, въведете местоживеене.'
        }
    )

    profile_pic = forms.ImageField(
        required=False,
        label='Профилна снимка'
    )



    class Meta:
        model = UserProfileInfo
        fields = ('phone_number', 'location', 'profile_pic')

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if UserProfileInfo.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("Този телефонен номер вече е използван.")
        return phone_number

    def clean(self):
        cleaned_data = super().clean()
        user_type = cleaned_data.get('user_type')
        profile_pic = cleaned_data.get('profile_pic')

        if user_type == 'volunteer' and not profile_pic:
            self.add_error('profile_pic', 'Доброволците трябва да качат профилна снимка.')
        return cleaned_data
