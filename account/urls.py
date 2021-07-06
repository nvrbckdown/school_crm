from django.urls import path, include
from . import views

urlpatterns = [
    path('students/', views.get_students, name='students'),
    path('students/<int:id>', views.get_student, name='student'),
    path('students-delete/<int:id>', views.delete_student, name='delete-student'),
    path('teachers/', views.get_teachers, name='teachers'),
    path('teachers/<int:id>', views.get_teacher, name='teacher'),
    path('teachers-delete/<int:id>', views.delete_teacher, name='delete-teacher')
]