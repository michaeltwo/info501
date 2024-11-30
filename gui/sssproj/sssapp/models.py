from django.db import models

class PatientData(models.Model):
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    hgb = models.FloatField()
    mcv = models.FloatField()
    plt = models.FloatField()
    rbc = models.FloatField()
    wbc = models.FloatField()
    result = models.CharField(max_length=3)  # 'Yes' or 'No'
    accuracy = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Prediction: {self.result} (Age: {self.age}, Sex: {self.sex})"
