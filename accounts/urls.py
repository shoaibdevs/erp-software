from django.urls import path
from .views import *

urlpatterns = [
    path('login/', user_login, name='login'),
    path('panel/', panel, name='panel'),
    path('logout/', logout_view, name='logout_view'),
    path('panel/exam/list/', list_exam, name='list'),

]
