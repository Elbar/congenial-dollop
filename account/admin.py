from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser, Librarian
from django.contrib.auth.forms import UserChangeForm

# Register your models here.


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