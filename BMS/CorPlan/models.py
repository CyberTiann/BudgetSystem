from django.db import models

# Create your models here.
class annual(models.Model):
    sources_of_funds = models.CharField(max_length=255)

class quarter(models.Model):
    sources_of_funds = models.CharField(max_length=255)