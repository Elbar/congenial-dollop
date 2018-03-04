from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Librarian, Patron, Student, Faculty, Professor, TA, Instructor
from django.contrib.auth.forms import UserChangeForm

# Register your models here.


class BaseUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class BaseUserAdmin(UserAdmin):
    form = BaseUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('phone_number', 'address')}),
    )


class LibrarianAdmin(BaseUserAdmin):
    pass


class PatronAdmin(BaseUserAdmin):
    pass


class StudentAdmin(BaseUserAdmin):
    pass


class FacultyAdmin(BaseUserAdmin):
    pass


class ProfessorAdmin(BaseUserAdmin):
    pass


class TAAdmin(BaseUserAdmin):
    pass


class InstructorAdmin(BaseUserAdmin):
    pass


admin.site.register(User, BaseUserAdmin)
admin.site.register(Patron, PatronAdmin)
admin.site.register(Librarian, LibrarianAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(TA, TAAdmin)
admin.site.register(Instructor, InstructorAdmin)