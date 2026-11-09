from django.db import models

# Create your models here.

# Responsable

class Responsable(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    correo = models.EmailField(unique=True, null=False)
    rut = models.CharField(max_length=12, null=False)

    class Meta:
        verbose_name_plural = "Responsables"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} - {self.correo} - {self.rut}"


# Mascota

class Mascota(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    anio_nacimiento = models.IntegerField(null=False)
    especie = models.CharField(max_length=50, null=False)

    responsable = models.ForeignKey(
        Responsable,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = "Mascotas"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} - {self.especie} - {self.responsable}"

