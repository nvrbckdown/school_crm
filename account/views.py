from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Profile, Student, Parent, Teacher
from school.models import Course, Payment, School, Status
from .forms import StudentForm, TeacherForm
from .utils import get_salary_service, create_student_service, create_teacher_service, delete_student_service, \
    payment_service


# <----STUDENT---->
@login_required(login_url='auth/login')
def get_students(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            create_student_service(form=form)
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
    parent = Parent.objects.filter(student_id=student.pk).first()
    res = {
        "student": student,
        "course": course,
        "payment": payment,
        "parent": parent
    }
    return render(request, 'account/student.html', res)


@login_required(login_url='auth/login')
def paid_course(request, id):
    amount = request.POST.get('amount')
    payment = Payment.objects.get(id=id)
    payment_service(amount, payment)
    return get_student(request=request, id=payment.student_id)


@login_required(login_url='auth/login')
def delete_student(request, id):
    delete_student_service(id=id)
    return redirect('students')

# <----TEACHER---->

@login_required(login_url='auth/login')
def get_teachers(request):
    error = ""
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            create_teacher_service(form=form)
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
    salary = get_salary_service(school, course)
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

# <----PARENT---->
@login_required(login_url='auth/login')
def get_parent(request, id):
    parent = Parent.objects.get(id=id)
    students = Student.objects.filter(parents=parent)
    res = {
        "parent": parent,
        "students": students
    }
    return render(request, 'account/parent.html', res)


@login_required(login_url='auth/login')
def delete_parent(request, id):
    parent = Parent.objects.filter(pk=id).first()
    Profile.objects.filter(id=parent.user.pk).delete()
    return redirect('index')