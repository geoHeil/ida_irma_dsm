from django.db import models
from django.contrib.auth.models import User


# Collection of access modes
class AccessRegime(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


# Multiple dataset families grouped by origin and content
class Database(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    
    def __str__(self):
            return self.name


# A data source (table) for which access can be requested
class DatasetFamily(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    database = models.ForeignKey(Database, on_delete=models.CASCADE)
    access_regime = models.ForeignKey(AccessRegime, on_delete=models.PROTECT)
    
    def __str__(self):
            return self.name


# Achievements that can be unlocked in the process of requesting data
# TODO: might need ProjectAchievement seperately, which has to be achieved
# multiple times for different projects
class AccessAchievement(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    
    def __str__(self):
            return self.name


# The researchers and analysts who would like to access data
class Consumer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    # TODO: if achievements might expire, look at:
    # https://docs.djangoproject.com/en/3.0/topics/db/models/#extra-fields-on-many-to-many-relationships
    access_achievements = models.ManyToManyField(AccessAchievement)
    
    def __str__(self):
            return self.name


# Mode of access (remote, secure on-site access, etc.)
class AccessModeType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    
    def __str__(self):
            return self.name


# Degree of anonymization of the dataset families
class AccessModeAnonymization(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    
    def __str__(self):
            return self.name


# Research fields for an access mode (scientific, ESCB, etc.)
class AccessModeResearchField(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    
    def __str__(self):
            return self.name


# Description of what needs to be achieved for a dataset family to be accessed in a specific form
class AccessMode(models.Model):
    name = models.CharField(max_length=100)
    access_regime = models.ForeignKey(AccessRegime, on_delete=models.CASCADE)
    access_mode_type = models.ForeignKey(AccessModeType, on_delete=models.PROTECT)
    access_mode_anonymization = models.ForeignKey(AccessModeAnonymization, on_delete=models.PROTECT)
    access_mode_research_field = models.ForeignKey(AccessModeResearchField, on_delete=models.PROTECT)
    access_achievements = models.ManyToManyField(AccessAchievement)
    description = models.CharField(max_length=200)

    def __str__(self):
            return self.name


# Central entity for managing users and data access
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    project_lead = models.ForeignKey(Consumer, on_delete=models.PROTECT)

    def __str__(self):
            return self.name


# Sub-group in a project which contains users and data
class ProjectGroup(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    members = models.ManyToManyField(Consumer)
    data = models.ManyToManyField(DatasetFamily)
    access_mode_type = models.ForeignKey(AccessModeType, on_delete=models.PROTECT)
    access_mode_anonymization = models.ForeignKey(AccessModeAnonymization, on_delete=models.PROTECT)
    access_mode_research_field = models.ForeignKey(AccessModeResearchField, on_delete=models.PROTECT)

