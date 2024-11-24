from django import forms
from .models import PatientData

class PatientDataForm(forms.ModelForm):
    class Meta:
        model = PatientData
        fields = ['age', 'sex', 'crp', 'hgb', 'mcv', 'plt', 'rbc', 'wbc']
        widgets = {
            'sex': forms.Select(choices=[('Male', 'Male'), ('Female', 'Female')]),
        }
