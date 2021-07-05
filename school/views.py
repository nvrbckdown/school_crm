from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import School, Course
from account.models import Student, Profile, Teacher
from .models import Course

@login_required(login_url='auth/login')
def index(request):
    schools = School.objects.all().count()
    courses = Course.objects.all().count()
    students = Student.objects.all().count()
    teachers = Teacher.objects.all().count()
    user_admin = Profile.objects.get(pk=request.user.pk)
    if request.user.is_authenticated and user_admin.role == "Admin":
        res = {
            "number_of_schools": schools,
            "number_of_courses": courses,
            "number_of_students": students,
            "number_of_teachers": teachers,
        }
        return render(request, "index.html", res)
    else:
        return redirect('login')


@login_required(login_url='auth/login')
def get_courses(request):
    courses = Course.objects.all()
    res = {
        "courses": courses
    }
    return render(request, 'school/courses.html', res)