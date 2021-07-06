from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import School, Course
from account.models import Student, Profile, Teacher
from .forms import CourseForm, SchoolForm


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
    error = ''
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses')
        else:
            error = 'Something went wrong!'

    form = CourseForm()
    courses = Course.objects.all()
    res = {
        "courses": courses,
        "form": form,
        "error": error
    }
    return render(request, 'school/courses.html', res)


@login_required(login_url='auth/login')
def get_schools(request):
    error = ''
    if request.method == "POST":
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schools')
        else:
            error = 'Something went wrong!'

    form = SchoolForm()
    schools = School.objects.all()
    res = {
        "schools": schools,
        "form": form,
        "error": error
    }
    return render(request, 'school/schools.html', res)