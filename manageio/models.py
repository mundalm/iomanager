from django.db import models
from django.core.urlresolvers import reverse

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=10)
    tfmPrefix = models.CharField(max_length=10)
    docString = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('manageio:equipment-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
   

class Feature(models.Model):
    name = models.CharField(max_length=100)
    equipments = models.ManyToManyField(Equipment)
    is_tested = models.BooleanField(default=False)

    def __str__(self):
        return self.name