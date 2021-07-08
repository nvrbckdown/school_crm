from django.db import models
from django.contrib.auth.models import AbstractUser

class Profile(AbstractUser):
    USER_ROLE = (
        ('Admin', 'Administrator'),
        ('Moder', 'Moderator'),
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
        ('Parent', 'Parent'),
    )

    role = models.CharField(max_length=255, choices=USER_ROLE, default='Student')
    phone_number = models.CharField(max_length=13, default='+998', blank=True, null=True)

    def __str__(self):
        return self.username

class Teacher(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    school = models.ManyToManyField('school.School', related_name='teachers')

    def __str__(self):
        return self.user.username

class Student(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='student')
    school = models.ForeignKey('school.School', on_delete=models.CASCADE, related_name='student')
    course = models.ManyToManyField('school.Course', related_name='students')

    def __str__(self):
        return self.user.username


class Parent(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='parents')