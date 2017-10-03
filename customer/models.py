from django.db import models
from django.core.urlresolvers import reverse

class Customer(models.Model):
    name = models.CharField(max_length=100)
    docString = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('customer:customer-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name