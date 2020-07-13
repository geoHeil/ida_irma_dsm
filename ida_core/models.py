from django.db import models
from django.contrib.auth.models import User

# TODO: check whether access regime is needed at all?
# Description of how access to a dataset family can be permitted
# class AccessRegime(models.Model):
#    name = models.CharField(max_length=100)


# Multiple dataset families grouped by origin and content
class Database(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
            return self.name


# A data source (table) for which access can be requested
class DatasetFamily(models.Model):
    name = models.CharField(max_length=100)
    database = models.ForeignKey(Database, on_delete=models.CASCADE)
    
    def __str__(self):
            return self.database.name + "." + self.name


class AccessAchievement(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
            return self.name


# The researchers and analysts who would like to access data
class Consumer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    # TODO: if achievements might expire, look at:
    # https://docs.djangoproject.com/en/3.0/topics/db/models/#extra-fields-on-many-to-many-relationships
    access_achievements = models.ManyToManyField(AccessAchievement)
    
    def __str__(self):
            return self.name


# Types of access to a dataset family (e.g. not anonymized, anonymized, ...)
class AccessModeCategory(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
            return self.name

# Description of what needs to be achieved for a dataset family to be accessed in a specific form
class AccessMode(models.Model):
    name = models.CharField(max_length=100)
    access_mode_category = models.ForeignKey(AccessModeCategory, on_delete=models.PROTECT)
    dataset_family = models.ForeignKey(DatasetFamily, on_delete=models.CASCADE)
    access_achievements = models.ManyToManyField(AccessAchievement)

    def __str__(self):
            return self.name
