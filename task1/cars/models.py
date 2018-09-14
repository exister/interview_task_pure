from django.db import models
from django.contrib.postgres.fields import JSONField
from django.db.models import OuterRef, Subquery, Count
from django.db.models.functions import Cast
from django.contrib.postgres.fields.jsonb import KeyTextTransform

# Create your models here


class ColorManager(models.Manager):
    def get_cars_count(self):
        cars = Car.objects.annotate(
            color_id=Cast(
                KeyTextTransform('colorId', 'parameters'),
                models.IntegerField()
            )
        ).filter(
            color_id=OuterRef('pk')
        ).order_by().values('color_id')
        cars_agg = cars.annotate(total=Count('*')).values('total')
        return Color.objects.annotate(cars_count=Subquery(cars_agg))


class Color(models.Model):
    name = models.CharField(max_length=50)

    objects = ColorManager()


class Car(models.Model):
    parameters = JSONField()
