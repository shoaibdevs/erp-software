from django.shortcuts import render, redirect, HttpResponse
from .models import  Exam, Exam_result
from django.contrib.auth.decorators import login_required
from .forms import *
from django.shortcuts import get_list_or_404, get_object_or_404

# from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.edit import UpdateView 

class ExamUpdateView(UpdateView): 
    # specify the model you want to use 
    model = Exam
    form_class = ExamForm 
  
    # specify the fields 
    # fields = "__all__"
    template_name_suffix = '_update'
    # can specify success url 
    # url to redirect after successfully 
    # updating details 
    success_url =   "/panel/exam/list/"
@login_required
def exam_delete(request, id):

    arg = Exam.objects.get(id=id)
    arg.delete()

    return redirect("/panel/exam/list/") 






@login_required
def exam_type_delete(request, id):

    arg = ExamType.objects.get(id=id)
    arg.delete()

    return redirect("/panel/exam/exam-type/list/") 

@login_required
def exam(request):
    forms = ExamForm()
    if request.method == 'POST':
        forms = ExamForm(data=request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/panel/exam/list')
    return render(request, 'exam/form.html', {'forms' : forms})



@login_required
def exam_result(request):
    forms = ExamResult()
    if request.method == 'POST':
        forms = ExamResult(data=request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/panel/exam/result/list/')

    return render(request, 'exam/exam_result.html', {'forms' :forms})

@login_required
def exam_result_list(request):
    data = Exam_result.objects.all()
    return render(request, 'exam/exam_result_list.html', {'data' : data})
    
class ExamResultUpdateView(UpdateView): 
    model = Exam_result
    form_class = ExamResult 
  
    template_name_suffix = '_update'
    success_url =   "/panel/exam/result/list/"

@login_required
def exam_result_delete(request, id):

    arg = Exam_result.objects.get(id=id)
    arg.delete()

    return redirect("/panel/exam/result/list/") 