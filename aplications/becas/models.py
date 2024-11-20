from django.db import models

# Create your models here.

class Becas(models.Model):
    idBeca = models.AutoField(primary_key=True)  # AUTO_INCREMENT, NOT NULL
    nombreBeca = models.CharField(max_length=255, null=False)  # NOT NULL
    tipoBeca = models.CharField(max_length=20, null=False)  # NOT NULL
    bActivo = models.BooleanField(null=True)  # NULLABLE

    def __str__(self):
        return self.nombreBeca
