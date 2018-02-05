from django.db import models

class User(models.Model):
    first_name = models.Integer_Field
    last_name = models.CharField(max_length=30)