from django import forms
from .models import PatientData

class PatientDataForm(forms.Form):
    age = forms.IntegerField(label='Age', required=True)
    sex = forms.ChoiceField(label='Sex', choices=[('M', 'Male'), ('F', 'Female')], required=True)
    hgb = forms.FloatField(label='HGB', required=True)
    mcv = forms.FloatField(label='MCV', required=True)
    plt = forms.FloatField(label='PLT', required=True)
    rbc = forms.FloatField(label='RBC', required=True)
    wbc = forms.FloatField(label='WBC', required=True)