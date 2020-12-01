from django.db import models

class Capitulo(models.Model):
    clave = models.CharField('Clave',max_length=4,primary_key=True)
    nombre = models.CharField('Nombre',max_length=150)

    def __str__(self):
       return str(self.clave)+" - "+str(self.nombre)

class Partida(models.Model):
    clave = models.CharField('Clave',max_length=4,primary_key=True)
    nombre = models.CharField('Nombre',max_length=75)
    descripcion = models.CharField('Descripcion',max_length=1200)
    capitulo = models.ForeignKey('partidas.Capitulo',verbose_name='Capitulo',on_delete=models.CASCADE)

    def __str__(self):
       return str(self.clave)+" - "+str(self.nombre)