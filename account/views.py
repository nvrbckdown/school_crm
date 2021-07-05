from django.shortcuts import render, redirect
from django.core.serializers import serialize
from .models import Profile, Student, Parent
from school.models import Course, Payment

def get_students(request):
    students = Student.objects.all()
    res = {
        "students": students
    }
    return render(request, 'account/students.html', res)


def get_student(request, id):
    student = Student.objects.get(id=id)
    course = Course.objects.filter(student=student.pk)
    payment = Payment.objects.filter(student=student.pk)
    print(course)
    res = {
        "student": student,
        "course": course,
        "payment": payment
    }
    return render(request, 'account/student.html', res)


def delete_student(request, id):
    student = Student.objects.filter(pk=id).first()
    Profile.objects.filter(id=student.user.pk).delete()
    return redirect('students')

