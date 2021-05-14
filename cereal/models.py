from django.db import models

# Create your models here.
class CerealCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Cereal(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(CerealCategory, on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self):
        return self.name



class CerealImage(models.Model):
    image = models.CharField(max_length=9999, blank=True)
    cereal = models.ForeignKey(Cereal, on_delete=models.CASCADE)