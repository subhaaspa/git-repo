from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    profile_URL = models.URLField(blank=True)
    profile_image = models.ImageField(upload_to='profile_image',blank=True)

    def __str__(self):
        return self.user.name
