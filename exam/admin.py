from django.contrib import admin
from .models import  Exam, Exam_result, Exam_result2
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

# Register your models here.

admin.site.register(Exam)

# class ArrayModelAdmin(admin.ModelAdmin, DynamicArrayMixin):
#     list_display = ['marks']
#     pass


# admin.site.register(Exam_result2, ArrayModelAdmin)

@admin.register(Exam_result)
class Exam_resultAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'father_name', 'subject_name']
    class Meta:
        model = Exam_result
        fields = '__all__'

