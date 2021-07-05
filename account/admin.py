from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile, Teacher, Student, Parent

UserAdmin.fieldsets += (
    (None, {'fields': ('role', 'phone_number')}),
)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'role']

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['user']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'school']

class ParentAdmin(admin.ModelAdmin):
    list_display = ['student']

admin.site.register(Profile, UserAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Parent, ParentAdmin)
