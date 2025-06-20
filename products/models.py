from django.db import models
from django.shortcuts import reverse

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    active = models.BooleanField(default=True)
    price = models.PositiveIntegerField(default=0)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])

