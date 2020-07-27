from django.contrib import admin


from .models import AccessRegime, Database, DatasetFamily, AccessAchievement
from .models import Consumer, AccessModeType, AccessModeAnonymization, AccessModeResearchField
from .models import AccessMode, Project, ProjectGroup


class DatasetFamilyInline(admin.TabularInline):
    model = DatasetFamily
    show_change_link = True
    extra = 0


class AccessModeInline(admin.TabularInline):
    model = AccessMode
    show_change_link = True
    extra = 0


class AccessRegimeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [AccessModeInline]


class DatabaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [DatasetFamilyInline]


class DatasetFamilyAdmin(admin.ModelAdmin):
    list_display = ('name', 'database', 'description')


class AccessAchievementAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class ConsumerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


class AccessModeTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class AccessModeAnonymizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class AccessModeResearchFieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class AccessModeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class ProjectGroupInline(admin.TabularInline):
    readonly_fields = ('status',)
    model = ProjectGroup
    show_change_link = True
    extra = 0


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'project_lead')
    inlines = [ProjectGroupInline]


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

admin.site.site_header = 'IDA/IRMA/DSM administration'
