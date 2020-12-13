from django.db import models

# Create your models here.
class Point(models.Model):
    coordx = models.CharField(verbose_name="coordenada X", max_length=10)
    coordy = models.CharField(verbose_name="coordenada Y", max_length=10)
    valormax = models.CharField(verbose_name="valor maximo", max_length=35)
    valormin = models.CharField(verbose_name="valor minimo",max_length=35)
    valorprom = models.CharField(verbose_name="valor promedio", max_length=35)
    frecuencia = models.CharField(verbose_name="frecuencia de Valor maximo", max_length=35)

    def __str__(self):
        return "{0} : {1}: {2} ; {3} : {4} : {5}".format(self.coordx, self.coordy, self.valormax, self.valormin, self.valorprom, self.frecuencia)


    class Meta:
        verbose_name = "Punto Medio"
        verbose_name_plural = "Puntos Medios"


class Paremetrs(models.Model):
    sweeptime = models.CharField(verbose_name="tiempo de barrido", max_length=15)
    resolution = models.CharField(verbose_name="freciencia de resolucion", max_length=35)
    sample = models.CharField(verbose_name="muesta", max_length=20)
    central = models.CharField(verbose_name="frecuencia central", max_length=20)
    band = models.CharField(verbose_name="ancho de banda", max_length=20)

    def __str__(self):
        return "{0} : {1}: {2} ; {3} : {4}".format(self.sweeptime, self.resolution, self.sample, self.central, self.band)


    class Meta:
        verbose_name = "Parametro"
        verbose_name_plural = "Parametros"


class Specific(models.Model):
    frecmax = models.CharField(verbose_name="frecuencia maxima", max_length=15)
    frecmin = models.CharField(verbose_name="frecuencia minuma", max_length=15)
    maker = models.CharField(verbose_name="fabricante", max_length=35)

    def __str__(self):
        return "{0} : {1}: {2}".format(self.frecmax, self.frecmin, self.maker)

    class Meta:
        verbose_name = "Especificacion"
        verbose_name_plural = "Especificaciones"


class Antenna(models.Model):
    reference = models.CharField(verbose_name="referencia", max_length=12)
    power = models.CharField(verbose_name="frecuencia minuma", max_length=15)

    def __str__(self):
        return "{0} : {1}".format(self.reference, self.power)

    class Meta:
        verbose_name = "Antena"
        verbose_name_plural = "Antenas"


class Routes(models.Model):

    name = models.CharField(verbose_name="nombre", max_length=45, unique=True)
    points = models.CharField(verbose_name="numero de puntos", max_length=10)
    date = models.CharField(verbose_name="fecha", max_length=13)
    duration = models.CharField(verbose_name="duracion", max_length=15)

    def __str__(self):
        return "{0} : {1}: {2} ; {3}".format(self.name, self.points, self.date, self.duration)

    class Meta:
        verbose_name = "Ruta"
        verbose_name_plural= "Rutas"


class equipment(models.Model):
    routes = models.ForeignKey(Routes)
    policy = models.CharField(verbose_name="poliza", max_length=30, unique=True)
    purchase = models.CharField(verbose_name="compra", max_length=25)
    datepurch = models.CharField(verbose_name="fecha de compra", max_length=25)
    datemake = models.CharField(verbose_name="fecha de fabricacion", max_length=25)

    def __str__(self):
        return "{0} : {1}: {2} ; {3}".format(self.policy, self.purchase, self.datepurch, self.datemake)

    class Meta:
        verbose_name ="Equipamento"
        verbose_name_plural = "Equipamentos"