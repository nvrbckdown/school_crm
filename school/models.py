from django.db import models
from account.models import Teacher, Student


class Region(models.Model):
    name = models.CharField(max_length=255, default='Tashkent')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'


class Status(models.Model):
    rank = models.CharField(max_length=2)
    rank_number = models.IntegerField()
    salary_amount = models.IntegerField()

    def __str__(self):
        return self.rank

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'


class School(models.Model):
    name = models.CharField(max_length=255, default='Viento')
    number = models.IntegerField()
    region = models.ForeignKey(Region, on_delete=models.DO_NOTHING, related_name='region')
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
    director_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    phone_number = models.CharField(max_length=13, default="+99890", blank=True, null=True)
    students_number = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        verbose_name = 'School'
        verbose_name_plural = 'Schools'
        order_with_respect_to = 'status'

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='courses', blank=True, null=True)
    teacher = models.ManyToManyField(Teacher, related_name='courses')
    cost = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class Payment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='payments')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='payments')
    paid = models.BooleanField(default=False)
    amount = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.course.name)