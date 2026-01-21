from django.db import models
from academics.models import Enrollment

class AcademicRecord(models.Model):
    enrollment = models.OneToOneField(Enrollment, on_delete=models.CASCADE)
    marks = models.FloatField()
    grade = models.CharField(max_length=2)
    approved = models.BooleanField(default=False)
