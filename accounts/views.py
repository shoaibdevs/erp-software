from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import *
from student.models import *
from exam.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def error_404_view(request, exception):
    return HttpResponse('Website is under construtcion')


def user_login(request):
    if request.user.is_authenticated and request.user.is_active and request.user.is_superuser:
            return redirect('/panel')
    if (request.method == 'POST'):
        username = request.POST.get('username') #Get email value from form
        password = request.POST.get('password') #Get password value from form
        user = authenticate(request, username=username, password=password)
        
        if user is not None:

            if user.is_active and user.is_superuser:
                login(request, user)
                return redirect('/panel')
            else:
                return redirect('/')
        return redirect('/')

    return render(request, 'registration/login.html')
    

# def panel(request):
#     return render(request, 'base/base.html')


            

# @login_required
def logout_view(request):
    logout(request)
    return redirect('/login')

@login_required
def panel(request):
    # franchise = FranchiseRegistration.objects.count()
    user = User.objects.count()
    new = Courses.objects.count()
    subject = Subject.objects.count()
    student = Student.objects.count()

    context = {
        'new' : new,
        'user' : user,
        'subject' : subject,
        'student' : student,

    }
    return render(request, 'home.html', context)
@login_required
def list_exam(request):
    data = Exam.objects.all()
    return render(request, 'exam/list.html', {'data' : data})
