from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_students, name='students'),
    path('<int:id>', views.get_student, name='student'),
    path('delete/<int:id>', views.delete_student, name='delete-student'),
    path('', include('django.contrib.auth.urls'))
]