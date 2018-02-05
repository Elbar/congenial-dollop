from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    libraryCard = models.CharField(max_length=200)


class Librarian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Patron(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
