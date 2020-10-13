from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.

from django.db import models


class Item(models.Model):
    CURRENCY = (
        ("ru", 'RUB'),
        ("us", 'USD'),
    )

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    currency = models.CharField(
        max_length=2,
        choices=CURRENCY,
        default="ru",
    )


class Order(models.Model):
    items = ArrayField(models.IntegerField(), default=list)
    total = models.IntegerField(default=0)
    # использование ManyToManyField увеличит число БД, усложнит доступ к данным, будет
    # делать много запросов при их получении и являеться избыточным для нашей задачи
