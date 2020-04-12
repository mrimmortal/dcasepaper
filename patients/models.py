from django.db import models

class Patient(models.Model):
    pid = models.IntegerField(blank=False)
    name = models.CharField(max_length=90, blank=False, default='')
    address = models.CharField(max_length=90, blank=False, default='')
    pmobile = models.CharField(max_length=20, blank=False, default='')
    age = models.IntegerField(blank=False, default='')
    dob = models.CharField(max_length=90, blank=False, default='')
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Casepaper(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    cid = models.IntegerField(blank=False, default=1)
    ctype = models.CharField(max_length=90, blank=False, default='')
