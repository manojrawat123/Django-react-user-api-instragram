from rest_framework import serializers
from myapp.models import Student, StudentMessges

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [ "id", "name", "img"]


class StudentMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentMessges
        fields = ["id", "name", "img", "my_status"]