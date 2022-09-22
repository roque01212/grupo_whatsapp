from django.db import models

# Create your models here.


class Servicio(models.Model):
    """Model definition for Servicio."""
    nombre = models.CharField('Nombre del servicio', max_length=20)
    importe = models.IntegerField()
    fecha_pago = models.DateField( auto_now_add=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Servicio."""

        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self):
        """Unicode representation of Servicio."""
        return f"{self.nombre} {self.id}"

class Alumno(models.Model):
    """Model definition for Alumnos."""

    nombre = models.CharField('Nombre:', max_length=20)
    apellido = models.CharField('Apellido:', max_length=10)
    dni = models.CharField('DNI:', max_length=20)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    # Servicio = models.ManyToManyField(Servicio)
    fecha = models.DateField( auto_now_add=True)
    hora = models.DateTimeField(auto_now_add=True)


    class Meta:
        """Meta definition for Alumnos."""

        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'

    def __str__(self):
        """Unicode representation of Alumnos."""
        return f"{self.nombre} {self.id}"