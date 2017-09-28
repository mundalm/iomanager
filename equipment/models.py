from django.db import models

class Equipment(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
   

class Feature(models.Model):
    name = models.CharField(max_length=100)
    equipments = models.ManyToManyField(Equipment)
    is_tested = models.BooleanField(default=False)

    def __str__(self):
        return self.name