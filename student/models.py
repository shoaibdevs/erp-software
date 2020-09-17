from django.db import models
from accounts.models import *

# Create your models here.



class Courses(models.Model):
    name = models.CharField(max_length=254)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class AcademicYear(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

class CourseSubject(models.Model):
    course = models.ForeignKey('Courses', on_delete=models.CASCADE)
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='documents/student-photo/', blank=True, null=True)
    admission_date = models.DateField()
    DOB = models.DateField()
    course = models.ForeignKey('Courses', on_delete=models.CASCADE, default=False)
    academic_year = models.ForeignKey('AcademicYear', on_delete=models.CASCADE, default=False)
    gender_choice = [
        ('1', 'Male'),
        ('2', 'Female')
    ]
    gender = models.CharField(max_length=4, choices=gender_choice)
    blood_group = models.CharField(max_length=20)
    religion = models.CharField(max_length=254)
    national_id = models.CharField(max_length=254)
    previous_school_information = models.CharField(max_length=254)
    previous_school_name = models.CharField(max_length=254)
    previous_class = models.CharField(max_length=254)
    previous_certificate = models.FileField(upload_to='documents/certificate/', blank=True, null=True)
    mother_name = models.CharField(max_length=254)
    father_name = models.CharField(max_length=254)
    health_condition_certificate = models.FileField(upload_to='documents/health', blank=True, null=True)

    def __str__(self): 
        return self.user.username



class Class(models.Model):
    name = models.CharField(max_length=254, unique=True)
    
    def __str__(self):
        return self.name
    
class Section(models.Model):
    name = models.CharField(max_length=254)
    Class = models.ForeignKey('Class', on_delete=models.SET_NULL, default=False, blank=True,null=True)

    def __str__(self):
        return self.name



class Subject(models.Model):
    name = models.CharField(max_length=254)
    Class = models.ForeignKey('Class', on_delete=models.SET_NULL, default=False, null=True)

    def __str__(self):
        return self.name

class Session(models.Model):
    name = models.CharField(max_length=254, unique=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name