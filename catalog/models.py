from django.db import models

import uuid # Required for unique book instances
# Create your models here.


class Document(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    release = models.DateField()
    edition = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=100000, decimal_places=2)
    thumbnailUrl = models.CharField(max_length=150)
    numberOfCopies = models.IntegerField(default=1)

    def __str__(self):
        return self.title


class JournalArticle(Document):
    journal = models.CharField(max_length=50)


class Video(Document):
    videoUrl = models.CharField(max_length=150)


class Book(Document):
    isbn = models.CharField(max_length=50)

