from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Card(models.Model):
    create_date = models.DateField(auto_now_add=True)


class Position(models.Model):
    card_id = models.ForeignKey(Card, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    latitud = models.DecimalField(max_digits=4, decimal_places=2,
                                  validators=[MinValueValidator(-90.00), MaxValueValidator(90.00)])
    longitud = models.DecimalField(max_digits=5, decimal_places=2,
                                   validators=[MinValueValidator(-180.00), MaxValueValidator(180.00)])
