from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Librarian, Patron, Student, Faculty, Professor, TA, Instructor
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


class MyLibrarianAdmin(MyUserAdmin):
    pass


admin.site.register(User, MyUserAdmin)
admin.site.register(Patron)
admin.site.register(Librarian, MyLibrarianAdmin)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Professor)
admin.site.register(TA)
admin.site.register(Instructor)