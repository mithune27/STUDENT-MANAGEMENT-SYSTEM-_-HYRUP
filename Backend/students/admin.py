from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "first_name", "course", "year", "status")
    search_fields = ("student_id", "first_name", "course")
    list_filter = ("status", "year")
