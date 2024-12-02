from django.shortcuts import render, redirect
from .forms import PatientDataForm
from .model import model
from .models import PatientData
import numpy as np
import xgboost

def predict(request):
    result = None
    accuracy = None

    if request.method == 'POST':
        form = PatientDataForm(request.POST)
        if form.is_valid():
            # Extract form data
            age = form.cleaned_data['age']
            sex = form.cleaned_data['sex']
            hgb = form.cleaned_data['hgb']
            mcv = form.cleaned_data['mcv']
            plt = form.cleaned_data['plt']
            rbc = form.cleaned_data['rbc']
            wbc = form.cleaned_data['wbc']

            # Prepare the input for the model
            sex_numeric = 1 if sex == 'M' else 0
            input_data = np.array([[age, sex_numeric, hgb, mcv, plt, rbc, wbc]])

            # Make prediction
            prediction = model.predict(input_data)
            accuracy = model.score(input_data, prediction)  # Adjust as needed

            result = 'Yes' if prediction[0] == 1 else 'No'

            # Save the input and output to the database
            PatientData.objects.create(
                age=age,
                sex=sex,
                hgb=hgb,
                mcv=mcv,
                plt=plt,
                rbc=rbc,
                wbc=wbc,
                result=result,
                accuracy=accuracy
            )

    else:
        form = PatientDataForm()

    return render(request, 'index.html', {'form': form, 'result': result, 'accuracy': accuracy})