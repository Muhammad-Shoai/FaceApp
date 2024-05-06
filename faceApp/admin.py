from django.contrib import admin
from .models import Student, Teacher, Subject, Attendance, FaceData

# Register your models here
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Attendance)
admin.site.register(FaceData)


admin.site.site_title = 'FaceApp administration'
admin.site.site_header = 'FaceApp administration'