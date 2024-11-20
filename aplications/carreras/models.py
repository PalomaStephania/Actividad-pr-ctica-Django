from django.db import models

# Create your models here.

class Carreras(models.Model):
    idCarrera = models.AutoField(primary_key=True)
    cveCarrera = models.CharField(max_length=10, unique=True, null=False)
    nombreCarrera = models.CharField(max_length=255, null=False)
    areaCarrera = models.CharField(max_length=30, null=False)
    planEstudios = models.CharField(max_length=30, null=False)
    bActivo = models.BooleanField(null=True)

    def __str__(self):
        return self.nombreCarrera
