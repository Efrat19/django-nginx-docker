from django.db import models

# Create your models here.

class Emoji(models.Model):
    unicode = models.CharField(max_length=10)
    description = models.CharField(max_length=30)

