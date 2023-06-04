from django.db import models
from django.urls import reverse


class Type(models.Model):
    class Meta:
        verbose_name = "Вид тура"
        verbose_name_plural = "Виды туров"

    name = models.CharField(max_length=255, verbose_name="Вид тура")
    slug = models.SlugField(max_length=255, db_index=True, unique=True)

    def get_absolute_url(self):
        return reverse("tourism", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name


class Images(models.Model):
    class Meta:
        verbose_name = "Фото для тура"
        verbose_name_plural = "Фото для туров"
    
    name = models.CharField(max_length=255, verbose_name="Место на фото")
    img = models.ImageField(upload_to="gallery", verbose_name="Фото")

    def __str__(self):
        return self.name


class TourGallery(models.Model):
    class Meta:
        verbose_name = "Галерея тура"
        verbose_name_plural = "Галереи туров"
    name = models.CharField(max_length=255, verbose_name="Название тура")
    images = models.ManyToManyField(Images, verbose_name="Фотографии")

    def __str__(self):
        return self.name


class TourExp(models.Model):
    class Meta:
        verbose_name = "Дополнительные расходы"
        verbose_name_plural = "Дополнительные расходы"
    name = models.CharField(max_length=255, verbose_name="Название расхода")
    price = models.PositiveIntegerField(verbose_name="Цена")

    def __str__(self):
        return f'{self.name} - {self.price}'

class Tour(models.Model):
    class Meta:
        verbose_name = "Тур"
        verbose_name_plural = "Туры"
    
    name = models.CharField(max_length=255, verbose_name="Название тура")
    image = models.ImageField(upload_to="images", verbose_name="Фото")
    type_of_tour = models.ForeignKey(Type, on_delete=models.DO_NOTHING, verbose_name="Вид тура")
    place = models.CharField(max_length=255, verbose_name="Место проведения тура")
    price = models.PositiveIntegerField(verbose_name="Цена тура за одного человека")
    time = models.CharField(max_length=255, verbose_name="Длительность тура")
    description = models.TextField(verbose_name="Описание экскурсии")
    description2 = models.TextField(verbose_name="Описание маршрута (каждую точку писать с новой строки!)")
    additional_plces = models.TextField(verbose_name="Далее на выбор (каждую точку писать с новой строки!)", blank=True, null=True)
    gallery = models.ForeignKey(TourGallery, on_delete=models.CASCADE, verbose_name="Галлерея")
    additional_expences = models.ManyToManyField(TourExp, verbose_name="Дополнительные расходы")
    fav = models.BooleanField(verbose_name="Добавить в популярные туры", default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("single_tour", kwargs={"pk": self.pk})
