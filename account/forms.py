from . import models
from django import forms
from school.models import School, Course

class StudentForm(forms.Form):
    CHOICES = School.objects.all().values_list("id", "name")
    COURSES = Course.objects.all().values_list("id", "name")
    username = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'AnvarYusupov'}
    ))
    password = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Viento@1'}
    ))
    last_name = forms.CharField(label="Lastname",max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Yusupov'}
    ))
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Anvar'}
    ))
    phone_number = forms.CharField(max_length=13, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': '+998*********'}
    ))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'ayusupov@gmail.com'}
    ))
    school = forms.ChoiceField(choices=CHOICES)
    course = forms.MultipleChoiceField(choices=COURSES)


class TeacherForm(forms.Form):
    CHOICES = School.objects.all().values_list("id", "name")
    username = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'AnvarYusupov'}
    ))
    password = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Viento@1'}
    ))
    last_name = forms.CharField(label="Lastname",max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Yusupov'}
    ))
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Anvar'}
    ))
    phone_number = forms.CharField(max_length=13, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': '+998*********'}
    ))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'ayusupov@gmail.com'}
    ))
    school = forms.MultipleChoiceField(choices=CHOICES)