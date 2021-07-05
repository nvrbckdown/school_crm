from . import models
from django.forms import ModelForm

class SchoolForm(ModelForm):
    class Meta:
        model = models.School
        fields = ['name', 'number', 'status', 'region']


class StatusForm(ModelForm):
    class Meta:
        model = models.Status
        fields = ['rank', 'rank_number', 'salary_amount']


class RegionForm(ModelForm):
    class Meta:
        model = models.Region
        fields = ['name']