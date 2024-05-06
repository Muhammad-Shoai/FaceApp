from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Student, Teacher, Attendance, Subject, FaceData
from .serializers import (
    AttendanceSerializer,
    StudentSignupSerializer,
    StudentSigninSerializer,
    StudentMarkAttendanceSerializer,
    StudentViewAttendanceSerializer,
    TeacherSignupSerializer,
    TeacherSigninSerializer,
    TeacherViewAttendanceReportSerializer,
    FaceDataSerializer,
)
class FaceDataListCreateView(generics.ListCreateAPIView):
    queryset = FaceData.objects.all()
    serializer_class = FaceDataSerializer

class FaceDataRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FaceData.objects.all()
    serializer_class = FaceDataSerializer

class StudentSignupView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSignupSerializer

class StudentSigninView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = StudentSigninSerializer(data=request.data)
        if serializer.is_valid():
            # Implement your authentication logic here
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

# Add views for marking and viewing attendance for students
class StudentMarkAttendanceView(CreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = StudentMarkAttendanceSerializer

class StudentViewAttendanceView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentViewAttendanceSerializer

# Add more views as needed for your specific functionalities.

class TeacherSignupView(CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSignupSerializer

class TeacherSigninView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TeacherSigninSerializer(data=request.data)
        if serializer.is_valid():
            # Implement your authentication logic here
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

class TeacherViewAttendanceReportView(ListAPIView):
    serializer_class = TeacherViewAttendanceReportSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        teacher = self.request.user  # Assuming the authenticated user is a teacher
        return Subject.objects.filter(teacher=teacher)

# Add more views as needed for your specific functionalities.
