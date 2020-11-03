from django import forms
from . import models

class AddStaff(forms.ModelForm):
    class Meta:
        model = models.Staffs
        fields = ['name', 'birthday', 'nrc',
                  'weight','height', 'birthplace', 'education',
                  'experience','appoint_date', 'photo',
                  'phone', 'marital','address', 'slug']