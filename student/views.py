from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse
from accounts.models import *
from .forms import *
from django.views.generic.edit import UpdateView 

from django.contrib.auth.decorators import login_required

# Create your views here.

class StudentUpdateView(UpdateView): 
    # specify the model you want to use 
    model = Student
    form_class = StudentForm 
  
    # specify the fields 
    # fields = "__all__"
    template_name_suffix = '_update'
    # can specify success url 
    # url to redirect after successfully 
    # updating details 
    success_url =   "/panel/student/show/"

# @superuser_only
@login_required
def student_delete(request, id):

    arg = Student.objects.get(id=id)
    arg.delete()

    return redirect("/panel/student/show/") 





class SubjectUpdateView(UpdateView): 
    # specify the model you want to use 
    model = Courses
    form_class = CourseForm 
  
    # specify the fields 
    # fields = "__all__"
    template_name_suffix = '_update'
    # can specify success url 
    # url to redirect after successfully 
    # updating details 
    success_url =   "/panel/student/subject/list/'"

# @superuser_only
@login_required
def subject_delete(request, id):

    arg = Courses.objects.get(id=id)
    arg.delete()

    return redirect("/panel/student/subject/list/") 

class SessionUpdateView(UpdateView): 
    # specify the model you want to use 
    model = AcademicYear
    form_class = SessionForm 
  
    # specify the fields 
    # fields = "__all__"
    template_name_suffix = '_update'
    # can specify success url 
    # url to redirect after successfully 
    # updating details 
    success_url =   "/panel/student/session/list/'"

# @superuser_only
@login_required
def session_delete(request, id):

    arg = AcademicYear.objects.get(id=id)
    arg.delete()

    return redirect("/panel/student/session/list/") 

@login_required
def student_register(request):
    forms = SignUpForm()
    # form = UserForm()

    if request.method == 'POST':
        forms = SignUpForm(data=request.POST , files=request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('/panel/student/show/')
    

    return render(request, 'student/registration.html', { 'forms' : forms })
    
@login_required
def show(request):
    data = Student.objects.all()
    return render(request, 'student/show.html', {'data' : data})



@login_required
def session_create(request):
    forms = SessionForm()
    if request.method == 'POST':
        forms = SessionForm(data=request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/panel/student/session/list/')
    return render(request, 'session/form.html', {'forms' : forms})

@login_required
def session_list(request):
    data = AcademicYear.objects.all()
    return render(request, 'session/list.html', {'data' : data})

@login_required
def subject_create(request):
    forms = CourseForm()
    if request.method == 'POST':
        forms = CourseForm(data=request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/panel/student/course/list/')
    
    return render(request, 'class/course/form.html', {'forms' : forms})
@login_required
def subject_list(request):
    data = Courses.objects.all()
    return render(request, 'class/course/list.html', {'data' : data})

@login_required
def coursesubject_create(request):
    forms = SubjectForm()
    if request.method == 'POST':
        forms = SubjectForm(data=request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/panel/student/subject/list/')
    
    return render(request, 'class/section/form.html', {'forms' : forms})

@login_required
def coursesubject_list(request):
    data = CourseSubject.objects.all()
    return render(request, 'class/section/list.html', {'data' : data})



