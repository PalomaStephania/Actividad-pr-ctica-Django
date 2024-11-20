from django.db import models

# Create your models here.

class EncargadoBecas(models.Model):
    idEncargado = models.AutoField(primary_key=True)  
    nombreEncargado = models.CharField(max_length=255, null=False)  
    numeroTrabajador = models.CharField(max_length=20, unique=True, null=False) 
    bActivo = models.BooleanField(null=True)  

    def __str__(self):
        return self.nombreEncargado

