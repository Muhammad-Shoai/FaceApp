from rest_framework import serializers
from .models import Student, Teacher, Attendance, Subject, FaceData

class FaceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaceData
        fields = ['roll_number', 'face_embeddings']
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['date', 'status']

class StudentSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'roll_number', 'password', 'program', 'semester']

class StudentSigninSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['roll_number', 'password']

class StudentMarkAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['date', 'status', 'subject']

class StudentViewAttendanceSerializer(serializers.ModelSerializer):
    subject_attendance = AttendanceSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ['name', 'roll_number', 'program', 'semester', 'subject_attendance']

class TeacherSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['name', 'teacher_id', 'password']

class TeacherSigninSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['teacher_id', 'password']

class TeacherViewAttendanceReportSerializer(serializers.ModelSerializer):
    subject_attendance = AttendanceSerializer(many=True, read_only=True)

    class Meta:
        model = Subject
        fields = ['name', 'subject_attendance']

# Adjust the fields and relationships based on your actual models and requirements.
