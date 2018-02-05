from django.db import models
from django.contrib.auth.models import (
    AbstractUser
)


class MyUser(AbstractUser):
    libraryCard = models.CharField(max_length=200)


class Librarian(models.Model):
    type = models.OneToOneField('MyUser', on_delete='DO_NOTHING')