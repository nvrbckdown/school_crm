from .models import Profile, Student, Teacher
from school.models import Payment, School, Status


def get_salary_service(school, course):
    salary = 0
    for s in school:
        salary = salary + s.status.rank_number
    for c in course:
        salary = salary + (c.cost * 0.3)
    return salary


def get_school_category(student_number):
    ranks = Status.objects.order_by('rank_number')
    for rank in ranks:
        if student_number <= rank.rank_number:
            return rank
    return ranks[-1]

def create_student_service(form):
    new_student = Profile.objects.create_user(
        username=form.cleaned_data.get('username'),
        email=form.cleaned_data.get('email'),
        first_name=form.cleaned_data.get('first_name'),
        last_name=form.cleaned_data.get('last_name'),
        password=form.cleaned_data.get('password'),
        phone_number=form.cleaned_data.get('phone_number'))
    school = School.objects.filter(name=form.cleaned_data.get('school')).first()
    student = Student.objects.create(user_id=new_student.id, school=school)
    student.course.set(form.cleaned_data.get('course'))
    student.save()
    courses = form.cleaned_data.get('course')
    for c in courses:
        payment = Payment.objects.create(student=student, course_id=c)
        payment.save()

    number = school.students_number
    school.students_number = number + 1
    school.status = get_school_category(number + 1)
    school.save()


def create_teacher_service(form):
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


def delete_student_service(id):
    student = Student.objects.filter(pk=id).first()
    school = student.school
    school.students_number -=1
    school.status = get_school_category(school.students_number - 1)
    school.save()
    Profile.objects.filter(id=student.user.pk).delete()
