from django.contrib import admin
from .models import *


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')


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


@admin.register(Copy)
class CopyAdmin(admin.ModelAdmin):
    list_display = ('document', 'room', 'level')


@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('document', 'room', 'level')