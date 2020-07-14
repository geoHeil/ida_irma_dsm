from django.contrib import admin

from .models import Database, DatasetFamily, AccessAchievement, Consumer, AccessModeType, AccessModeAnonymization, AccessModeResearchField, AccessMode


class DatasetFamilyInline(admin.TabularInline):
    model = DatasetFamily
    show_change_link = True
    extra = 0


class AccessModeInline(admin.TabularInline):
    model = AccessMode
    show_change_link = True
    extra = 0


class DatabaseAdmin(admin.ModelAdmin):
    inlines = [DatasetFamilyInline]


class DatasetFamilyAdmin(admin.ModelAdmin):
    inlines = [AccessModeInline]


admin.site.register(Database, DatabaseAdmin)
admin.site.register(DatasetFamily, DatasetFamilyAdmin)
admin.site.register(AccessAchievement)
admin.site.register(Consumer)
admin.site.register(AccessModeType)
admin.site.register(AccessModeAnonymization)
admin.site.register(AccessModeResearchField)
admin.site.register(AccessMode)

admin.site.site_header = 'IDA/IRMA/DSM administration'
