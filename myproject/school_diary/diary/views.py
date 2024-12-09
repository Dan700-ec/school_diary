from django.shortcuts import render, get_object_or_404
from .models import Student

def home(request):
    students = Student.objects.all()
    return render(request, 'diary/home.html', {'students': students})

def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'diary/student_detail.html', {'student': student})
