from django.contrib import admin
# from .models import 
from .models import Courses, CourseSubject, Student, AcademicYear

# Register your models here.

# admin.site.register(StudentRegistration)
# admin.site.register(Class)
# admin.site.register(Session)
# admin.site.register(Section)
# admin.site.register(Subject)
# admin.site.register(Student)

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ['name','price', 'id']
    class Meta:
        model = Courses
        fields = '__all__'


@admin.register(CourseSubject)
class CourseSubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'course', 'id']
    class Meta:
        model = CourseSubject
        fields = '__all__'


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'DOB', 'id']
    class Meta:
        model = Student
        fields = '__all__'


@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):
    
    class Meta:
        model = AcademicYear
        fields = '__all__'
