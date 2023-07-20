from django.db import models

class Consultant(models.Model):
   name = models.CharField(max_length=255)
   specialization = models.CharField(max_length=64)
   def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=16)
    def __str__(self):
        return self.name

class Appointment(models.Model):
    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_appointment = models.DateField()
    comment = models.CharField(max_length=255)