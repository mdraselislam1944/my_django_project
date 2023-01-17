from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.http import HttpResponse
from .serializer import EmployeeSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import Employee

@csrf_exempt
def employee_list(request):
    if request.method=='GET':
        emps=Employee.objects.all()
        serialazer=EmployeeSerializer(emps,many=True)
        return JsonResponse(serialazer.data,safe=False)
    elif request.method=='POST':
        data=JSONParser().parse(request)
        serialazer=EmployeeSerializer(data=data)
        if serialazer.is_valid():
            serialazer.save()
            return JsonResponse(serialazer.data,status=201)
        return JsonResponse(serialazer.errors,status=400)
    

@csrf_exempt
def employee_detail(request,pk):
    try:
        employee=Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return HttpResponse(status=404)

    if request.method=='GET':
        serializer=EmployeeSerializer(employee)
        return JsonResponse(serializer.data)

    elif request.method=='PUT':
        data=JSONParser().parse(request)
        serializer=EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400)

    elif request.method=='DELETE':
        employee.delete()
        return HttpResponse(status=204)
    




    