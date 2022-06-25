from django.db import models

class Familiar(models.model):
    nombre_y_apellido = models.CharField(max_Length=30)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField(null=True)
    parentesco = models.CharField(max_Length=30)

