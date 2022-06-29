from django.db import models


class Edificio(models.Model):

    nombre = models.CharField("Nombre edificio", max_length=50)
    direccion = models.CharField("Direccion", max_length=80)
    ciudad = models.CharField("Ciudad", max_length=30)
    tipo_opciones = (
        ('residencial', 'Residencial'),
        ('comercial', 'Comercial'),
    )
    tipo = models.CharField(max_length=20, choices=tipo_opciones)

    def __str__(self):
        return "%s %s %s %s" % (self.nombre,
                                self.direccion,
                                self.ciudad,
                                self.tipo)


class Departamento(models.Model):

    propietario = models.CharField("Nombre propietario", max_length=30)
    costo = models.DecimalField(
        "Costo departamento", max_digits=100, decimal_places=2)
    Ncuartos = models.IntegerField("Numero cuartos")
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
                                 related_name="departamentos")

    def __str__(self):
        return "%s %s %s %s" % (self.propietario,
                                self.costo,
                                self.Ncuartos,
                                self.edificio)
