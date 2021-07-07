from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Profile, Student, Parent, Teacher
from school.models import Course, Payment, School, Status
from .forms import StudentForm, TeacherForm
from .utils import get_salary


# <----STUDENT---->
@login_required(login_url='auth/login')
def get_students(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student = Profile.objects.create_user(
                                   username=form.cleaned_data.get('username'),
                                   email=form.cleaned_data.get('email'),
                                   first_name=form.cleaned_data.get('first_name'),
                                   last_name=form.cleaned_data.get('last_name'),
                                   password=form.cleaned_data.get('password'),
                                   phone_number=form.cleaned_data.get('phone_number'))
            student = Student.objects.create(user_id=new_student.id, school_id=form.cleaned_data.get('school'))
            student.course.set(form.cleaned_data.get('course'))
            student.save()
            courses = form.cleaned_data.get('course')
            for c in courses:
                payment = Payment.objects.create(student=student, course_id=c)
                payment.save()
            school = School.objects.get(id=form.cleaned_data.get('school'))
            number = school.students_number
            school.students_number = number + 1
            school.save()
            return redirect('students')

    form = StudentForm()
    students = Student.objects.all()
    res = {
        "students": students,
        "form": form
    }
    return render(request, 'account/students.html', res)


@login_required(login_url='auth/login')
def get_student(request, id):
    student = Student.objects.get(id=id)
    course = Course.objects.filter(students=student.pk)
    payment = Payment.objects.filter(student=student.pk)
    res = {
        "student": student,
        "course": course,
        "payment": payment
    }
    return render(request, 'account/student.html', res)


@login_required(login_url='auth/login')
def paid_course(request, id):
    payment = Payment.objects.get(id=id)
    payment.paid = True
    payment.save()
    return get_student(request=request, id=payment.student_id)


@login_required(login_url='auth/login')
def delete_student(request, id):
    student = Student.objects.filter(pk=id).first()
    school = student.school
    school.students_number -=1
    school.save()
    Profile.objects.filter(id=student.user.pk).delete()

    return redirect('students')

# <----TEACHER---->

@login_required(login_url='auth/login')
def get_teachers(request):
    error = ""
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            new_teacher = Profile.objects.create(
                username=form.cleaned_data.get('username'),
                email=form.cleaned_data.get('email'),
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
                password=form.cleaned_data.get('password'),
                phone_number=form.cleaned_data.get('phone_number'),
                role='Teacher')
            teacher = Teacher.objects.create(user=new_teacher)
            teacher.school.set(form.cleaned_data.get("school"))
            teacher.save()
        else:
            error = "Something went wrong!"

    form = TeacherForm()
    teachers = Teacher.objects.all()
    res = {
        "teachers": teachers,
        "form": form,
        "error": error
    }
    return render(request, 'account/teachers.html', res)


@login_required(login_url='auth/login')
def get_teacher(request, id):
    teacher = Teacher.objects.get(id=id)
    course = Course.objects.filter(teacher=teacher.pk)
    school = School.objects.filter(teachers=teacher.id)
    salary = get_salary(school, course)
    res = {
        "teacher": teacher,
        "course": course,
        "school": school,
        "salary": salary
    }
    return render(request, 'account/teacher.html', res)


@login_required(login_url='auth/login')
def delete_teacher(request, id):
    teacher = Teacher.objects.filter(pk=id).first()
    Profile.objects.filter(id=teacher.user.pk).delete()
    return redirect('teachers')


@login_required(login_url='auth/login')
def edit_teacher(request, id):
    teacher = Teacher.objects.get(pk=id)
    form = TeacherForm(request.POST)
    res = {
        "form": form
    }
    return render(request, '', res)