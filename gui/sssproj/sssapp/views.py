from django.shortcuts import render, redirect
from .forms import PatientDataForm
from .models import PatientData

def diagnose_patient(request):
    if request.method == "POST":
        form = PatientDataForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            print(patient)
            # Example logic for diagnosis (replace with your actual logic)
            if patient.crp > 10 or patient.wbc > 11:
                patient.diagnosis = "Potential Infection"
            elif patient.hgb < 12:
                patient.diagnosis = "Anemia"
            else:
                patient.diagnosis = "Healthy"
            patient.save()
            return render(request, 'diagnosis_result.html', {'patient': patient})
    else:
        form = PatientDataForm()
    return render(request, 'diagnose_patient.html', {'form': form})

def index(request):
    return render(request, 'index.html', {'test': 'test'})
