from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Librarian, Patron
from django.contrib.auth.forms import UserChangeForm

# Register your models here.


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('libraryCard',)}),
    )


admin.site.register(User, MyUserAdmin)
admin.site.register(Patron)
admin.site.register(Librarian)
