from django.contrib import admin


from .models import AccessRegime, Database, DatasetFamily, AccessAchievement
from .models import Consumer, AccessModeType, AccessModeAnonymization, AccessModeResearchField
from .models import AccessMode, Project, ProjectGroup, AchievementRelation
from .models import ResearcherType


class DatasetFamilyInline(admin.TabularInline):
    model = DatasetFamily
    show_change_link = True
    extra = 0


class AccessModeInline(admin.TabularInline):
    model = AccessMode
    show_change_link = True
    extra = 0


class ResearcherTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


class AccessRegimeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [AccessModeInline]


class DatabaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [DatasetFamilyInline]


class DatasetFamilyAdmin(admin.ModelAdmin):
    list_display = ('name', 'database', 'description')


class AccessAchievementAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'isLinkedToProject', 'isLinkedToConsumer', 'get_achievement_type_str')
    readonly_fields = ('get_achievement_type_str',)


class ConsumerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'researcher_type')


class AccessModeTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class AccessModeAnonymizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class AccessModeResearchFieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class AccessModeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class ProjectGroupInline(admin.TabularInline):
    readonly_fields = ('get_status_access_mode', 'get_status_requirements', 'get_status_achievements', 'get_status_message')
    model = ProjectGroup
    show_change_link = True
    extra = 0


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'project_lead')
    inlines = [ProjectGroupInline]


class AchievementRelationAdmin(admin.ModelAdmin):
    list_display = ('achievement', 'consumer', 'project')


admin.site.register(ResearcherType, ResearcherTypeAdmin)
admin.site.register(AccessRegime, AccessRegimeAdmin)
admin.site.register(Database, DatabaseAdmin)
admin.site.register(DatasetFamily, DatasetFamilyAdmin)
admin.site.register(AccessAchievement, AccessAchievementAdmin)
admin.site.register(Consumer, ConsumerAdmin)
admin.site.register(AccessModeType, AccessModeTypeAdmin)
admin.site.register(AccessModeAnonymization, AccessModeAnonymizationAdmin)
admin.site.register(AccessModeResearchField, AccessModeResearchFieldAdmin)
admin.site.register(AccessMode, AccessModeAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(AchievementRelation, AchievementRelationAdmin)

admin.site.site_header = 'IDA/IRMA/DSM administration'
