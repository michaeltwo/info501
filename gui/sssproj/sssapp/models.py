from django.db import models

class PatientData(models.Model):
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    crp = models.FloatField()
    hgb = models.FloatField()
    mcv = models.FloatField()
    plt = models.FloatField()
    rbc = models.FloatField()
    wbc = models.FloatField()
    diagnosis = models.CharField(max_length=255)

    def __str__(self):
        return f"Diagnosis: {self.diagnosis} (ID: {self.id})"
