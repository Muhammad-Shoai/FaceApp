from django.urls import path
from .views import (
    StudentSignupView,
    StudentSigninView,
    StudentMarkAttendanceView,
    StudentViewAttendanceView,
    TeacherSignupView,
    TeacherSigninView,
    TeacherViewAttendanceReportView,
    FaceDataListCreateView,
    FaceDataRetrieveUpdateDestroyView,
)

urlpatterns = [
    # Student URLs
    path('students/signup/', StudentSignupView.as_view(), name='student-signup'),
    path('students/signin/', StudentSigninView.as_view(), name='student-signin'),
    path('students/mark-attendance/', StudentMarkAttendanceView.as_view(), name='student-mark-attendance'),
    path('students/view-attendance/', StudentViewAttendanceView.as_view(), name='student-view-attendance'),
    path('facedata/', FaceDataListCreateView.as_view(), name='facedata-list-create'),
    path('facedata/<str:pk>/', FaceDataRetrieveUpdateDestroyView.as_view(), name='facedata-detail'),
    # Teacher URLs
    path('teachers/signup/', TeacherSignupView.as_view(), name='teacher-signup'),
    path('teachers/signin/', TeacherSigninView.as_view(), name='teacher-signin'),
    path('teachers/view-attendance-report/', TeacherViewAttendanceReportView.as_view(), name='teacher-view-attendance-report'),
]

# Add more paths as needed for your specific functionalities.
