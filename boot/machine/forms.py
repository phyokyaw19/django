from django import forms
from . import models

class addmachine(forms.ModelForm):
    class Meta:
        model = models.machines
        fields = '__all__'

class updatemachine(forms.ModelForm):
    class Meta:
        model = models.machines
        fields = '__all__'




