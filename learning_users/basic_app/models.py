from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # Add any additional attributes you want
    
    # pip install pillow to use this!
    # Optional: pip install pillow --global-option=”build_ext” --global-option=”--disable-jpeg”
    profile_pic_d = models.ImageField(upload_to='profile_pics',blank=True)
    profile_pic_p=models.ImageField(upload_to='profile_pics',blank=False)
    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username
