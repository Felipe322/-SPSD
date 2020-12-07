from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator,\
    MaxLengthValidator, RegexValidator


class Capitulo(models.Model):
    clave = models.IntegerField('Clave', primary_key=True, validators=[
                                MaxValueValidator(9000),
                                MinValueValidator(1000),
                                RegexValidator(regex='[1-9][0]{3,3}',
                                               message='Ingrese un capítulo válido')])
    nombre = models.CharField('Nombre', max_length=150)

    def __str__(self):
        return str(self.clave)+" - "+str(self.nombre)


class Partida(models.Model):
    clave = models.IntegerField('Clave', validators=[MaxValueValidator(
        9000), MinValueValidator(1000), RegexValidator(regex='[0-9]{4,4}',
                                                       message='Ingrese una partida válida')],
                                                        primary_key=True)
    nombre = models.CharField('Nombre', max_length=75)
    descripcion = models.CharField('Descripcion', max_length=1200, validators=[
                                   MaxLengthValidator(1200)])
    capitulo = models.ForeignKey(
        'partidas.Capitulo', verbose_name='Capitulo', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.clave)+" - "+str(self.nombre)
