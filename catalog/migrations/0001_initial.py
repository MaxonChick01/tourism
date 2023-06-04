# Generated by Django 4.2.1 on 2023-06-03 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Место на фото')),
                ('img', models.ImageField(upload_to='gallery', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Фото для тура',
                'verbose_name_plural': 'Фото для туров',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Вид тура')),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Вид тура',
                'verbose_name_plural': 'Виды туров',
            },
        ),
        migrations.CreateModel(
            name='TourGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название тура')),
                ('images', models.ManyToManyField(to='catalog.images', verbose_name='Фотографии')),
            ],
            options={
                'verbose_name': 'Галерея тура',
                'verbose_name_plural': 'Галереи туров',
            },
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название тура')),
                ('image', models.ImageField(upload_to='images', verbose_name='Фото')),
                ('place', models.CharField(max_length=255, verbose_name='Место проведения тура')),
                ('price', models.PositiveIntegerField(verbose_name='Цена тура за одного человека')),
                ('time', models.CharField(max_length=255, verbose_name='Длительность тура')),
                ('description', models.TextField(verbose_name='Описание экскурсии')),
                ('description2', models.TextField(verbose_name='Описание маршрута (каждую точку писать с новой строки!)')),
                ('additional_plces', models.TextField(blank=True, null=True, verbose_name='Далее на выбор (каждую точку писать с новой строки!)')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.tourgallery', verbose_name='Галлерея')),
                ('type_of_tour', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.type', verbose_name='Вид тура')),
            ],
            options={
                'verbose_name': 'Тур',
                'verbose_name_plural': 'Туры',
            },
        ),
    ]