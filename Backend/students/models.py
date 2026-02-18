

# Create your models here.
from django.db import models
from django.conf import settings


class Student(models.Model):
    STATUS_CHOICES = (
        ("active", "Active"),
        ("graduated", "Graduated"),
        ("dropped", "Dropped"),
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="student_profile"
    )

    student_id = models.CharField(max_length=20, unique=True)

    # Personal Info
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    # Academic Info
    course = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    gpa = models.DecimalField(max_digits=4, decimal_places=2)
    credits_earned = models.PositiveIntegerField(default=0)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="active"
    )

    # Contact Info
    phone = models.CharField(max_length=15)
    address = models.TextField()

    # Soft delete
    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student_id} - {self.first_name}"
