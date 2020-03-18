from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Additional Classes
    portfolio_site = models.URLField(blank=True)  # User does not have to fill out site
    profile_pic = models.ImageField(upload_to='profile_pics',
                                    blank=True)  # Create sub-directory profile_pics in media directory

    def __str__(self):
        return self.user.username


