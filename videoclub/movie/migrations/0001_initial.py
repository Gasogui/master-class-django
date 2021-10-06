# Generated by Django 3.2.8 on 2021-10-06 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=4, verbose_name='Código')),
                ('title', models.CharField(max_length=50, verbose_name='Titulo')),
                ('year', models.PositiveIntegerField(max_length=4, verbose_name='Año')),
                ('time', models.PositiveIntegerField(max_length=4, verbose_name='Duración ')),
                ('lang', models.CharField(max_length=50, verbose_name='Lenguaje')),
                ('date_pre', models.DateField(blank=True, null=True, verbose_name='Premier')),
                ('pre_Country', models.CharField(max_length=5, verbose_name='País')),
                ('fecha_ingreso', models.DateField(auto_now_add=True, verbose_name='Fecha de ingreso')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de modificación')),
            ],
            options={
                'verbose_name': 'Película',
                'verbose_name_plural': 'Películas',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=4, verbose_name='Código')),
                ('title', models.CharField(max_length=20, verbose_name='Titulo')),
                ('movie_id', models.ManyToManyField(to='movie.Movie', verbose_name='Película(s)')),
            ],
        ),
    ]