from datetime import datetime, timedelta

from django.db import models

from account.models import User, Faculty


class Document(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    release = models.DateField(auto_now=True)
    edition = models.IntegerField(default=1)
    price = models.DecimalField(default=0, max_digits=100000, decimal_places=2)
    thumbnailUrl = models.CharField(max_length=150)
    copies_count = models.IntegerField(default=1)

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

    def checkout_duration(self, user, document):
        if user in Faculty.__dict__:
            return timedelta(28)
        elif self.bestseller and document in JournalArticle.__dict__ and document in Audio.__dict__ and document in Video.__dict__:
            return timedelta(14)
        else:
            return timedelta(21)


class Checkout(models.Model):
    document = models.OneToOneField(Document, on_delete=models.DO_NOTHING)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    since = models.DateField(auto_now=True)
    until = models.DateField(default=datetime.now()+Book(document).checkout_duration(user, document))

    def __str__(self):
        return self.document.title + " checked out by " + self.user.first_name + " " + self.user.last_name
