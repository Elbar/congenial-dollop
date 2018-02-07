from django.contrib import admin
from .models import Document, JournalArticle, Video, Book, Checkout,Audio

# Register your models here.

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
# Register the Admin classes for BookInstance using the decorator


@admin.register(JournalArticle)
class JournalArticleAdmin(DocumentAdmin):
    pass


@admin.register(Video)
class VideoAdmin(DocumentAdmin):
    pass


@admin.register(Audio)
class AudioAdmin(DocumentAdmin):
    pass


@admin.register(Book)
class BookAdmin(DocumentAdmin):
    pass


@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    pass
