from django.db import models


class HomeWork(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=700)
    date = models.ImageField('hw/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

