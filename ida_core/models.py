from django.db import models

class Consumer(models.Model):
    name = models.CharField(max_length=200)
