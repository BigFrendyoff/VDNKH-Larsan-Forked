import uuid

from django.db import models


class Place(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    order = models.IntegerField(verbose_name='Порядок')
    name = models.CharField(max_length=150, verbose_name='Название')
    pic_url = models.CharField(max_length=150)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)


class Route(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=150, verbose_name='Название')
    code = models.CharField(max_length=50, verbose_name='Код')
    places = models.ManyToManyField(Place, related_name='route', verbose_name='Места')
    pic_url = models.URLField()
    detail_pic_url = models.URLField()

    @property
    def points(self):
        return len(self.places)

    def __str__(self):
        return self.name
