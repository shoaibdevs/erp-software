from django import forms  
from .models import *
from accounts.models import User
from bootstrap_datepicker_plus import DatePickerInput


user_types= [
        ('1', 'Franchise'),
        ('2', 'Student'),
        ('3', 'Admin')
    ]
class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length = 30, widget = forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your username'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}))
    photo = forms.ImageField(widget = forms.ClearableFileInput(attrs={'class': 'form-control'}))
    health_condition_certificate = forms.ImageField(widget = forms.ClearableFileInput(attrs={'class': 'form-control'}))
    previous_certificate = forms.ImageField(widget = forms.ClearableFileInput(attrs={'class': 'form-control'}))


    # password1 = forms.CharField(widget = forms.PasswordInput)
# ('user', 'photo', 'admission_date', 'DOB', 'course', 'academic_year', 'gender_choice', 'gender', 'blood_group', 'religion', 'national_id', 'previous_school_information', 'previous_school_name', 'previous_class', 'previous_certificate', 'mother_name', 'father_name', 'health_condition_certificate', )
    class Meta:
        model = Student
        exclude = ['user']
        widgets = {


            'admission_date': DatePickerInput().start_of('admission_date'),
            'father_name': forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Enter Your Father Name'}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Enter Your Mother Name'}),
            'religion': forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Enter Your Religion'}),
            'national_id': forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Enter Your National ID'}),
            'previous_school_information': forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Enter Your Previous School Information'}),
            'previous_school_name': forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Enter Your Prevoius School Name'}),
            'previous_class': forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Enter Your Previous Class Name'}),


            'DOB': DatePickerInput().start_of('DOB'),
            'gender': forms.Select(attrs={'class': 'form-control', 'placeholder' : 'Select you gender'}),
            'blood_group': forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Enter Your Blood Group'}),
            'academic_year': forms.Select(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),

            # 'Session': forms.Select(attrs={'class': 'form-control'}),
            
            
            # 'Subject' : forms.CheckboxSelectMultiple()
        }

    def clean_username(self): # check if username does not exist before
        try:
            User.objects.get(username=self.cleaned_data['username']) #get user from user model
        except User.DoesNotExist :
            return self.cleaned_data['username']

        raise forms.ValidationError("This user exist already choose an0ther username")


    def save(self): # create new user
        new_user = User.objects.create_user(username=self.cleaned_data['username'],password=self.cleaned_data['password'])
        new_user.save()
        UserProf =  super(SignUpForm,self).save(commit = False)
        UserProf.user = new_user
        UserProf.save()
        return UserProf


class CourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Enter Course Name'}),
            'price' : forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Enter Price of the course'})
        }

class SessionForm(forms.ModelForm):
    class Meta:
        model = AcademicYear
        fields = "__all__"
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Enter Session'}),
               
        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model = CourseSubject
        fields = "__all__"
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Enter Subject Name'}),
            'course' : forms.Select(attrs={'class': 'form-control'})   
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['photo', 'admission_date', 'DOB', 'course', 'academic_year',  'gender', 'blood_group', 'religion', 'national_id', 'previous_school_information', 'previous_school_name', 'previous_class', 'previous_certificate', 'mother_name', 'father_name', 'health_condition_certificate']
        widgets = {


            'admission_date': DatePickerInput().start_of('admission_date'),
            'father_name': forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Enter Your Father Name'}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Enter Your Mother Name'}),
            'religion': forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Enter Your Religion'}),
            'national_id': forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Enter Your National ID'}),
            'previous_school_information': forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Enter Your Previous School Information'}),
            'previous_school_name': forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Enter Your Prevoius School Name'}),
            'previous_class': forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Enter Your Previous Class Name'}),


            'DOB': DatePickerInput().start_of('DOB'),
            'gender': forms.Select(attrs={'class': 'form-control', 'placeholder' : 'Select you gender'}),
            'blood_group': forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Enter Your Blood Group'}),
            'academic_year': forms.Select(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),

        }
