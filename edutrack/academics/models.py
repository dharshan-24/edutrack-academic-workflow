from django.db import models
from accounts.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)
    semester = models.IntegerField()
    credits = models.IntegerField()

class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role':'STUDENT'})
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='ENROLLED')
