from django.shortcuts import render, get_object_or_404, redirect
from .forms import CreateStudentForm
from .models import Student
# Create your views here.


def CreateStudent(request):
    if request.method == "POST":
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            form = CreateStudentForm()
    else:
        form = CreateStudentForm()
    students = Student.objects.all().order_by("-id")
    context = {'form': form, 'students': students}
    return render(request, 'index.html', context)


def GetStudent(request, **kwargs):
    reg = kwargs.get('reg')
    student = get_object_or_404(Student, reg_no=reg)
    if request.method == "POST":
        form = CreateStudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
    else:
        form = CreateStudentForm(instance=student)
    context = {'student': student, 'form': form}
    return render(request, 'std_detail.html', context)


def DeleteStudent(request, **kwargs):
    reg = kwargs.get('reg')
    student = Student.objects.get(reg_no=reg)
    student.delete()
    return redirect(CreateStudent)
