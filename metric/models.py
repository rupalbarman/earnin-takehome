from django.db import models

class Metric(models.Model):
    slug = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, null=False, blank=True)
