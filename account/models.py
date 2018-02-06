from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    libraryCard = models.CharField(max_length=200)


class Librarian(User):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

    class Meta:
        verbose_name = 'Librarian'
        verbose_name_plural = 'Librarians'


class Patron(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

    class Meta:
        # verbose_name = 'Patron'
        verbose_name_plural = 'Patrons'


class Student(models.Model):
    user = models.OneToOneField(Patron, on_delete=models.CASCADE, primary_key=True)


class Faculty(models.Model):
    user = models.OneToOneField(Patron, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'


class Professor(models.Model):
    user = models.OneToOneField(Faculty, on_delete=models.CASCADE, primary_key=True)


class TA(models.Model):
    user = models.OneToOneField(Faculty, on_delete=models.CASCADE, primary_key=True)


class Instructor(models.Model):
    user = models.OneToOneField(Faculty, on_delete=models.CASCADE, primary_key=True)
