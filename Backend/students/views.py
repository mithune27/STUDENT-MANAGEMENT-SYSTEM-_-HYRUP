from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["first_name", "last_name", "student_id", "course"]
    ordering_fields = ["gpa", "year"]

    def get_queryset(self):
        user = self.request.user

        if user.role == "admin":
            return Student.objects.filter(is_deleted=False)

        return Student.objects.filter(user=user, is_deleted=False)

    def perform_destroy(self, instance):
        if self.request.user.role != "admin":
            raise PermissionDenied("Only admins can delete students.")
        instance.is_deleted = True
        instance.save()
