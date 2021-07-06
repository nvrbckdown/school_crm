from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/', views.get_courses, name='courses'),
    path('schools/', views.get_schools, name='schools'),
]