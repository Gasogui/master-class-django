from django.db import models

# Create your models here.


class Movie (models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField('Código', max_length=4, blank=False, null=False)
    title = models.CharField('Titulo', max_length=50, blank=False, null=False)
    year = models.PositiveIntegerField(
        'Año', max_length=4, blank=False, null=False)
    time = models.PositiveIntegerField(
        'Duración ', max_length=4, blank=False, null=False)
    lang = models.CharField('Lenguaje', max_length=50, blank=False, null=False)
    date_pre = models.DateField('Premier', blank=True, null=True)
    pre_Country = models.CharField(
        'País', max_length=5, blank=False, null=False)
    fecha_ingreso = models.DateField(
        'Fecha de ingreso', auto_now=False, auto_now_add=True)
    fecha_modificacion = models.DateField(
        'Fecha de modificación', auto_now=True)

    def __str__(self):
        return '%s' % (self.title)

    class Meta:
        ordering = ['title']
        verbose_name = 'Película'
        verbose_name_plural = 'Películas'


class Genres (models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField('Código', max_length=4, blank=False, null=False)
    title = models.CharField('Titulo', max_length=20, blank=False, null=False)
    movie_id = models.ManyToManyField(Movie, verbose_name='Película(s)')

    def __str__(self):
        return '%s' % (self.title)

    class Meta:
        ordering = ['title']
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'
