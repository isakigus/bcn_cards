from __future__ import unicode_literals

from django.db import models


class Card(models.Model):
    create_date = models.DateField()


class Position(models.Model):
    card_id = models.ForeignKey(Card, on_delete=models.CASCADE)
    create_date = models.DateField()
    latitud = models.DecimalField(max_digits=2, decimal_places=2)
    longitud = models.DecimalField(max_digits=3, decimal_places=2)
