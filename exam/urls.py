from django.urls import path
from . import views

urlpatterns = [
    # path('test/', views.test, name='test'),
    path('exam/create/', views.exam, name='exam'),
    
    path('exam/update/<pk>/', views.ExamUpdateView.as_view()),
    path('exam/delete/<id>/', views.exam_delete),


    path('exam/result/update/<pk>/', views.ExamResultUpdateView.as_view()),
    path('exam/result/delete/<id>/', views.exam_result_delete),

    path('exam/result/create/', views.exam_result, name='exam_result'),
    path('exam/result/list/', views.exam_result_list, name='exam_result_list'),

    



]