from django import forms  
from .models import *
from bootstrap_datepicker_plus import DatePickerInput
# from .widgets import SplitJSONWidget
from multivaluefield import MultiValueField

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Exam Name'}),
            'start_date' : DatePickerInput().start_of('start_date'),
        }

class ExamResult(forms.ModelForm):
    # subject = forms.MultiValueField(forms.Select(attrs={'class': 'form-control'}))
    # marks = forms.MultiValueField(forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' Enter Student marks'}))

    class Meta:
        model = Exam_result
        fields = "__all__"
        widgets = {
            'student' : forms.Select(attrs={'class': 'form-control'}),
            'course' : forms.Select(attrs={'class': 'form-control'}),

            'subject' : forms.Select(attrs={'class': 'form-control'}),
            'marks' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' Enter Student marks'})

        }

