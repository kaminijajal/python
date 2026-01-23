from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserImage(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="user_images/")
