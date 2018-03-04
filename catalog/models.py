from datetime import datetime, timedelta

from django.contrib.contenttypes.models import ContentType
from django.db import models

from account.models import User, Faculty


class Document(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    release_year = models.DateField(max_length=50)
    edition = models.IntegerField(default=1)
    price = models.DecimalField(default=0, max_digits=100000, decimal_places=2)
    thumbnail_url = models.CharField(max_length=150)

    @staticmethod
    def checkout_duration(user, document):
        if user in Faculty.__dict__:
            return timedelta(28)
        elif Book(document).bestseller and document in JournalArticle.__dict__ and document in Audio.__dict__ \
                and document in Video.__dict__:
            return timedelta(14)
        else:
            return timedelta(21)

    def get_cname(self):
        class_name = ""
        if self in Book.__dict__:
            class_name = "Book"
        return class_name

    def get_copies_count(self):
        return Copy.objects.filter(document=self).count()

    def __str__(self):
        return self.title


class JournalArticle(Document):
    journal = models.CharField(max_length=50)


class Video(Document):
    videoUrl = models.CharField(max_length=150)


class Audio(Document):
    audioUrl = models.CharField(max_length=150)


class Book(Document):
    isbn = models.CharField(max_length=50)
    bestseller = models.BooleanField(default=False)


class Checkout(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    since = models.DateField(auto_now=True)
    until = models.DateField(default=datetime.now()+Document(document).checkout_duration(user, document))

    def __str__(self):
        return self.document.title + " checked out by " + self.user.first_name + " " + self.user.last_name


class Copy(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    room = models.CharField(max_length=200)
    level = models.CharField(max_length=200)

    def __str__(self):
        return "New copy of " + self.document.title + " added"

    class Meta:
        verbose_name = 'Copy'
        verbose_name_plural = 'Copies'


class Reference(models.Model):
    document = models.ForeignKey(Document, on_delete=models.DO_NOTHING)
    room = models.CharField(max_length=200)
    level = models.CharField(max_length=200)

    def __str__(self):
        return "New references of " + self.document.title + " added"
