from django.db import models

# Create your models here.

class Grupo(models.Model):
    idGrupo = models.AutoField(primary_key=True)
    cveGrupo = models.CharField(max_length=10, unique=True, null=False)
    nombreGrupo = models.CharField(max_length=20, null=False)
    cuatrimestreGrupo = models.CharField(max_length=30, null=False)
    aulaNombre = models.CharField(max_length=30, null=False)
    aulaUbicacion = models.CharField(max_length=100, null=False)
    bActivo = models.BooleanField(null=True)

    def __str__(self):
        return f"{self.cveGrupo} - {self.nombreGrupo}"
