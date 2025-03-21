from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from .validators import validate_phone_number



class UserProfileInfo(models.Model):
    USER_TYPES=[
     ('volunteer','patient')   
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(unique=True,validators=[validate_phone_number])
    location = models.CharField(max_length=100,blank=False,default='Unknown')
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
      

    def __str__(self):
        return f"{self.user.username} - {self.phone_number}"
