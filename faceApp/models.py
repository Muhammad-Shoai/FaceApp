from django.db import models

class Student(models.Model):
    roll_number = models.CharField(max_length=20, primary_key=True)  # Primary key
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    program = models.CharField(max_length=10, choices=[('IT', 'IT'), ('CS', 'CS'), ('SE', 'SE')])
    semester = models.IntegerField(choices=zip(range(1, 9), range(1, 9)))

    def __str__(self):
        return self.name
class FaceData(models.Model):
    roll_number= models.CharField(max_length=20, primary_key=True)
    face_embeddings=models.JSONField()

class Teacher(models.Model):
    teacher_id = models.CharField(max_length=20, primary_key=True)  # Primary key
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)  # Many-to-One: Many Subjects can have one Teacher
    students = models.ManyToManyField(Student)  # Many-to-Many: Many Subjects can be associated with many Students

    def __str__(self):
        return self.name

class Attendance(models.Model):
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('present', 'Present'), ('absent', 'Absent')])
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # Many-to-One: Many Attendances can have one Student
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)  # Many-to-One: Many Attendances can have one Subject

    def __str__(self):
        return f"{self.student.name} - {self.subject.name} - {self.date}"
