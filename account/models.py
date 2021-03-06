from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def get_queryset(self):
        if Patron.objects.filter(username=self.username).exists():
            return 'Patron'
        elif Librarian.objects.filter(username=self.username).exists():
            return 'Librarian'
        return 'User'


class Librarian(User):
    class Meta:
        verbose_name = 'Librarian'
        verbose_name_plural = 'Librarians'


class Patron(User):
    class Meta:
        verbose_name = 'Patron'
        verbose_name_plural = 'Patrons'


class Student(Patron):
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'


class Faculty(Patron):
    class Meta:
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'


class Professor(Faculty):
    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professors'


class TA(Faculty):
    class Meta:
        verbose_name = 'Teaching Assistant'
        verbose_name_plural = 'Teaching Assistants'


class Instructor(Faculty):
    class Meta:
        verbose_name = 'Instructor'
        verbose_name_plural = 'Instructors'
