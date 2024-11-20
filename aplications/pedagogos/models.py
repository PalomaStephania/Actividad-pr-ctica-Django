from django.db import models

# Create your models here.

class Pedagogo(models.Model):
    idPedagogo = models.AutoField(primary_key=True)  # AUTO_INCREMENT, NOT NULL
    nombrePedagogo = models.CharField(max_length=255, null=False)  # NOT NULL
    numeroTrabajador = models.CharField(max_length=20, unique=True, null=False)  # UNIQUE, NOT NULL
    bActivo = models.BooleanField(null=True)  # NULLABLE

    def __str__(self):
        return self.nombrePedagogo
