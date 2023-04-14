
from django.db import models

class Medicine(models.Model):
    name = models.CharField(max_length=255)
    donation = models.CharField(max_length=255)
    days = models.CharField(max_length=255)
    observations = models.TextField()
    bibliography = models.TextField()
    color = models.CharField(max_length=25)

    def __str__(self):
        return self.name
