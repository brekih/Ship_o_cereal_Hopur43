from django.db import models
from cereal.models import Cereal

# Create your models here.

class tableCart(models.Model):
    IdCereal = models.ForeignKey(Cereal, on_delete=models.CASCADE)
    CerealAmount = models.IntegerField()

    def __str__(self):
        return (self.IdCereal.name)
