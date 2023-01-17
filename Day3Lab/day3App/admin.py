from django.contrib import admin

# Register your models here.
from day3App.models import Department,Employee

admin.site.register(Department)
admin.site.register(Employee)