from django.db import models
from django.contrib.auth.models import User

class Consumer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

class Database(models.Model):
    name = models.CharField(max_length=100)

class DatasetFamily(models.Model):
    name = models.CharField(max_length=100)
    database = models.ForeignKey(Database, on_delete=models.CASCADE)
