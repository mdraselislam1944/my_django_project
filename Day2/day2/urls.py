from django.urls import path
from .views import CreateEmployee, GetEmployee, DeleteEmployee, Home

urlpatterns = [
    path('', Home, name='home'),
    path('create/', CreateEmployee, name='create_new_emp'),
    path('emp_edit/<str:id>/', GetEmployee, name='emp_edit'),
    path('delete/<str:id>', DeleteEmployee, name='delete'),
]
