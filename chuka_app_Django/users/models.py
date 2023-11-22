from django.db import models
from django.contrib.auth.models import User


class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50, null=True, blank=True)
    lastname = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True, null=False, blank=False)
    profile_picture = models.ImageField(
        upload_to="/profiles", default="avatar.jpg", verbose_name="profile"
    )

    def get_profile_picture(self):
        return self.profile_picture.url

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
