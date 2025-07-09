from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    symptoms = models.TextField()

    def __str__(self):
        return f"{self.name} (Age: {self.age})"

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return f"Dr. {self.name} - {self.specialization}"

class PatientDoctorMapping(models.Model):  # ✅ Renamed from "Mapping" to match serializer
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.patient.name} → {self.doctor.name}"
