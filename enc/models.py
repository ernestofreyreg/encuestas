from django.db import models

# Create your models here.
from encuestas.settings import SERVER_DOMAIN


class Encuesta(models.Model):
    nombre = models.CharField(max_length=100)
    datos = models.TextField()
    vigente = models.BooleanField()

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = "Encuesta"
        verbose_name_plural = "Encuestas"


class Imagen(models.Model):
    archivo = models.FileField(upload_to='imagenes')

    def __unicode__(self):
        return "Imagen %d"%(self.id)

    class Meta:
        verbose_name = "Imagen"
        verbose_name_plural = "Imagenes"

    def imageurl(self):
        return "http://%s/img/%d"%(SERVER_DOMAIN, self.id)




