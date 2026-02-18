from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ["is_deleted"]

    def validate_gpa(self, value):
        if value < 0 or value > 10:
            raise serializers.ValidationError("GPA must be between 0 and 10.")
        return value
