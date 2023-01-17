from django.shortcuts import render
# Create your views here.
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Employee

from django.http import HttpResponse
from django.template import loader


class EmployeeBaseView(View):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('day3App:all')


class EmployeeListView(EmployeeBaseView, ListView):
    model = Employee
    template_name = "employee_list.html"
    fields = '__all__'
    success_url = reverse_lazy('day3App:all')


class EmployeeDetailView(EmployeeBaseView, DetailView):
    model = Employee
    template_name = "employee_detail.html"
    fields = '__all__'
    success_url = reverse_lazy('day3App:all')


class EmployeeCreateView(EmployeeBaseView, CreateView):
    model = Employee
    template_name = "employee_form.html"
    fields = '__all__'
    success_url = reverse_lazy('day3App:all')


class EmployeeUpdateView(EmployeeBaseView, UpdateView):
    model = Employee
    template_name = "employee_form.html"
    fields = '__all__'
    success_url = reverse_lazy('day3App:all')


class EmployeeDeleteView(EmployeeBaseView, DeleteView):
    model = Employee
    template_name = "employee_confirm_delete.html"
    fields = '__all__'
    success_url = reverse_lazy('day3App:all')
