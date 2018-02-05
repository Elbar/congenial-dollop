from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, BookInstance, MyUser, Librarian
from django.contrib.auth.forms import UserChangeForm

# Register your models here.

# admin.site.register(Book)
# admin.site.register(BookInstance)

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = MyUser


class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('libraryCard',)}),
    )


admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Librarian)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
# Register the Admin classes for BookInstance using the decorator


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass
