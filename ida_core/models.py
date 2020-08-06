from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

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


# Researcher Type: intern or extern
class ResearcherType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Achievements that can be unlocked in the process of requesting data
class AccessAchievement(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    isLinkedToConsumer = models.BooleanField(verbose_name='always linked to a specific consumer')
    isLinkedToProject = models.BooleanField(verbose_name='always linked to a specific project')
    
    def __str__(self):
            return self.name
    
    def get_achievement_type_str(self):
        if (self.isLinkedToConsumer):
            if (self.isLinkedToProject):
                return "all"
            else:
                return "per researcher"
        else:
            if (self.isLinkedToProject):
                return "per project"
            else:
                return "invalid!"
    get_achievement_type_str.short_description = 'Achievement type'

# The researchers and analysts who would like to access data
class Consumer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    researcher_type = models.ForeignKey(ResearcherType, on_delete=models.PROTECT)
    
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
    access_mode_researcher_type = models.ForeignKey(ResearcherType, on_delete=models.PROTECT)
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
    access_mode_research_field = models.ForeignKey(AccessModeResearchField, on_delete=models.PROTECT)

    def __str__(self):
            return self.name


# Sub-group in a project which contains users and data
class ProjectGroup(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    members = models.ManyToManyField(Consumer)
    dataset_families = models.ManyToManyField(DatasetFamily)
    access_mode_type = models.ForeignKey(AccessModeType, on_delete=models.PROTECT)
    access_mode_anonymization = models.ForeignKey(AccessModeAnonymization, on_delete=models.PROTECT)
    access_mode_researcher_type = models.ForeignKey(ResearcherType, on_delete=models.PROTECT)

    def generate_status(self):
        # Get required achievements and check whether there are suitable access
        # modes available for all dataset families.
        dsf = self.dataset_families.all()
        required_achievements = []
        suitable_access_modes = True
        message = ""
        for i in dsf:
            access_regime = i.access_regime
            access_modes = access_regime.accessmode_set.filter(access_mode_type=self.access_mode_type).filter(access_mode_anonymization=self.access_mode_anonymization).filter(access_mode_researcher_type=self.access_mode_researcher_type).filter(access_mode_research_field=self.project.access_mode_research_field)
            if access_modes.count() == 0:
                suitable_access_modes = False
                message = message + f"{i} has no suitable access mode available for {self.access_mode_type}/{self.access_mode_anonymization}/{self.access_mode_researcher_type}/{self.project.access_mode_research_field}.\n"
            else:
                required_achievements.extend(access_modes.last().access_achievements.all())
        if (suitable_access_modes == False):
            return {
                'data_access': False,
                'requirements': message,
                'achievements': False,
                'message': message
            }
        for m in self.members.all():
            if m.researcher_type != self.access_mode_researcher_type:
                suitable_access_modes = False
                message = message + f"{m} is not {self.access_mode_researcher_type}!\n"
        if (suitable_access_modes == False):
            return {
                'data_access': False,
                'requirements': message,
                'achievements': False,
                'message': message
            }
        # If there is an access mode for every dataset family, we can continue.
        # Next, we have to check whether every member has all required
        # achievements.
        required_achievements = set(required_achievements)
        requirements_str = "\n".join(["- " + str(a) + " (" + a.get_achievement_type_str() +")" for a in required_achievements])
        achievements_fulfilled = True
        message = "Missing achievements!\n"
        for m in self.members.all():
            available_member_achievements = set([a.achievement for a in AchievementRelation.objects.filter(consumer=m).filter(Q(project=self.project) | Q(project__isnull=True))])
            available_project_achievements = set([a.achievement for a in AchievementRelation.objects.filter(project=self.project).filter(consumer__isnull=True)])
            available_achievements = available_member_achievements | available_project_achievements
            missing_achievements = required_achievements - available_achievements
            if len(missing_achievements) > 0:
                achievements_fulfilled = False
                message = message + str(m) + ":\n" + "\n".join(["- " + str(a) for a in missing_achievements]) +"\n\n"
        if (achievements_fulfilled == False):
            return {
                'data_access': True,
                'requirements': requirements_str,
                'achievements': False,
                'message': message
            }
        else:
            return {
                'data_access': True,
                'requirements': requirements_str,
                'achievements': True,
                'message': "Requirements fulfilled."
            }
    
    def get_status_access_mode(self):
        return self.generate_status()['data_access']
    get_status_access_mode.boolean = True
    get_status_access_mode.short_description = 'Access mode possible?'

    def get_status_requirements(self):
        return self.generate_status()['requirements']
    get_status_requirements.short_description = 'Access requirements'

    def get_status_achievements(self):
        return self.generate_status()['achievements']
    get_status_achievements.boolean = True
    get_status_achievements.short_description = 'Requirements fullfilled?'
    
    def get_status_message(self):
        return self.generate_status()['message']
    get_status_message.short_description = 'Status'


# Assignment of an achievement
class AchievementRelation(models.Model):
    achievement = models.ForeignKey(AccessAchievement, null=True, blank=True, on_delete=models.PROTECT)
    consumer = models.ForeignKey(Consumer, null=True, blank=True, on_delete=models.PROTECT)
    project = models.ForeignKey(Project, null=True, blank=True, on_delete=models.PROTECT)
    # TODO: add valid from and valid to
