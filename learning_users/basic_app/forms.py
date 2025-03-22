from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo,Settlement
from phonenumber_field.formfields import PhoneNumberField  
from basic_app.validators import custom_pass_validation
from basic_app.validators import validate_phone_number
from django import forms



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


    profile_pic = forms.ImageField(
        required=False,
        label='Профилна снимка'
    ) 

    location = forms.ModelChoiceField(
        queryset=Settlement.objects.all().order_by('name'),
        to_field_name='name',
        empty_label="Изберете село",
        label="Населено място (село)",
        widget=forms.Select(attrs={'class': 'village-select'}))
    

    class Meta:
        model = UserProfileInfo
        fields = ('phone_number', 'profile_pic',  'user_type', 'location')




   


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
