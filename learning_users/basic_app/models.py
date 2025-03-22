from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from .validators import validate_phone_number



class UserProfileInfo(models.Model):
    USER_TYPES=[
    ('patient', 'Patient'),
    ('volunteer', 'Volunteer'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(unique=True,validators=[validate_phone_number])
    location = models.CharField(max_length=100,default='Unknown')
    municipality = models.CharField(max_length=100,default='Unknown')
    region = models.CharField(max_length=100,default='Unknown')
    
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='patient')
    assigned_patients = models.ManyToManyField('self', symmetrical=False, related_name='assigned_volunteers', blank=True)


    def __str__(self):
        return f"{self.user.username} ({self.user_type})"


    def __str__(self):
        return f"{self.user.username} - {self.phone_number}"
    

class Settlement(models.Model):
    name = models.CharField(max_length=100)
    municipality = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

