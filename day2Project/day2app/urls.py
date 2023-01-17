from django.urls import path
from .views import *

urlpatterns = [
    path('', CreateStudent, name='create_student'),
    path('std_detail/<str:reg>/', GetStudent, name='std_detail'),
    path('delete/<str:reg>', DeleteStudent, name='delete'),
    path('update/<str:reg>', UpdateStudent, name='update'),
]
