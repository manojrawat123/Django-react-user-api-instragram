from django.contrib import admin
from myapp.models import Student, StudentMessges


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name","img"]


@admin.register(StudentMessges)
class StudentMessageAdmin(admin.ModelAdmin):
    list_display = ["id", "name","img", "my_status"]



