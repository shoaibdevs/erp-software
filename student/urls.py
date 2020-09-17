from django.urls import path
from . import views

urlpatterns = [
    path('student/update/<pk>/', views.StudentUpdateView.as_view()),
    path('student/delete/<id>/', views.student_delete),

    # path('student/section/update/<pk>/', views.SectionUpdateView.as_view()),
    # path('student/section/delete/<id>/', views.section_delete),

    path('student/session/update/<pk>/', views.SessionUpdateView.as_view()),
    path('student/session/delete/<id>/', views.session_delete),

    path('student/subject/update/<pk>/', views.SubjectUpdateView.as_view()),
    path('student/subject/delete/<id>/', views.subject_delete),

    path('student/create/', views.student_register, name='student_register'),
    path('student/show/', views.show, name='student_show'),

    path('student/subject/create/', views.coursesubject_create, name='coursesubject_create'),
    path('student/subject/list/', views.coursesubject_list, name='coursesubject_list'),

    # path('student/section/list/', views.section_list, name='section_list'),
    path('student/session/create/', views.session_create, name='session_create'),
    path('student/session/list/', views.session_list, name='session_list'),
    path('student/courses/create/', views.subject_create, name='course_create'),
    path('student/courses/list/', views.subject_list, name='course_list'),
    # path('student/class/ajax/,', views.load_Class, name='load_class_ajax')




]