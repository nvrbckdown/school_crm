from django.contrib import admin
from .models import School, Status, Region, Course, Payment

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'status', 'region')
    list_filter = ('status', 'region')

class StatusAdmin(admin.ModelAdmin):
    list_display = ('rank', 'rank_number', 'salary_amount')

class RegionAdmin(admin.ModelAdmin):
    list_display = ('name',)

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'cost']

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['course', 'student']

admin.site.register(School, SchoolAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Payment, PaymentAdmin)
