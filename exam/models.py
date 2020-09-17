from django.db import models
from student.models import *
from student.models import  Courses
from django.contrib.postgres.fields import ArrayField
from django.db import models
from jsonfield import JSONField
from picklefield.fields import PickledObjectField
import uuid
from django_better_admin_arrayfield.models.fields import ArrayField

class Exam(models.Model):
    name = models.CharField(max_length=254)
    start_date = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.name

class Exam_result(models.Model):
    student = models.ForeignKey('student.Student',on_delete=models.CASCADE, default=False)
    course = models.ForeignKey('student.Courses', on_delete=models.CASCADE, default=False)
    subject = models.ForeignKey('student.CourseSubject', on_delete=models.CASCADE, default=False)
    marks = models.IntegerField()

    def __str__(self):
        return str(self.student)
    
    def student_name(self):
        return self.student.name
    def father_name(self):
        return self.student.father_name
    def subject_name(self):
        return self.subject.name
        
        
class Exam_result2(models.Model):
    student = models.ForeignKey('student.Student',on_delete=models.CASCADE, default=False)
    course = models.ForeignKey('student.Courses', on_delete=models.CASCADE, default=False)
    subject = models.ForeignKey('student.CourseSubject',related_name='subjectarry', on_delete=models.CASCADE, default=False)
    marks = ArrayField(models.CharField(max_length=20), blank=True, null=True)

    def __str__(self):
        return str(self.student)
    
    def student_name(self):
        return self.student.name
    def father_name(self):
        return self.student.father_name
    def subject_name(self):
        return self.subject.name
        

