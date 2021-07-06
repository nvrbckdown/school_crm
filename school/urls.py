from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/', views.get_courses, name='courses'),
    path('courses/<int:id>/', views.get_course, name='course'),
    path('courses/delete/<int:id>/', views.delete_course, name='delete-course'),
    path('schools/', views.get_schools, name='schools'),
    path('schools/<int:id>/', views.get_school, name='school'),
    path('schools/delete/<int:id>/', views.delete_school, name='delete-school')
]