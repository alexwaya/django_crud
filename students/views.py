from django.shortcuts import render
from .models import Student
from .forms import CreateStudentForm


def CreateStudent(request):
    if request.method == "POST":
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            form = CreateStudentForm()
    else:
        form = CreateStudentForm()

    students = Student.objects.all().order_by("-id")
    context = {'form':form, 'students':students}
    return render(request, 'home.html', context)