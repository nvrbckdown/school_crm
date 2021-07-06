from django.shortcuts import render, redirect
from .models import Profile, Student, Parent, Teacher
from school.models import Course, Payment, School
from .forms import StudentForm, TeacherForm

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
            print(courses)
            for c in courses:
                print(c)
                payment = Payment.objects.create(student=student, course_id=c)
                payment.save()
            return redirect('students')

    form = StudentForm()
    students = Student.objects.all()
    res = {
        "students": students,
        "form": form
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


def get_teacher(request, id):
    teacher = Teacher.objects.get(id=id)
    course = Course.objects.filter(teacher=teacher.pk)
    print(teacher.school.all())
    res = {
        "teacher": teacher,
        "course": course
    }
    return render(request, 'account/teacher.html', res)


def delete_teacher(request, id):
    teacher = Teacher.objects.filter(pk=id).first()
    Profile.objects.filter(id=teacher.user.pk).delete()
    return redirect('teachers')