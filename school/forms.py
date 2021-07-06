from . import models
from django.forms import ModelForm, TextInput, Select, MultipleChoiceField, NumberInput

class SchoolForm(ModelForm):
    class Meta:
        model = models.School
        fields = ['name', 'number', 'status', 'region']

        widgets = {
            'name': TextInput(
                attrs={'class': 'form-control',
                        'placeholder': 'Name'}),
            'number': NumberInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Number'}),
            'status': Select(
                attrs={'class': 'form-control'}),
            'region': Select(
                attrs={'class': 'form-control'})
        }

class CourseForm(ModelForm):
    class Meta:
        model = models.Course
        fields = ['name', 'school', 'teacher', 'cost']

        widgets = {
            'name': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Name'}),
            'school': Select(
                attrs={'class': 'form-control'}),
            'cost': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Cost'})
        }


class StatusForm(ModelForm):
    class Meta:
        model = models.Status
        fields = ['rank', 'rank_number', 'salary_amount']


class RegionForm(ModelForm):
    class Meta:
        model = models.Region
        fields = ['name']