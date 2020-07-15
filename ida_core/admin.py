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
    list_display = ('name', 'description')
    inlines = [DatasetFamilyInline]


class DatasetFamilyAdmin(admin.ModelAdmin):
    list_display = ('name', 'database', 'description')
    inlines = [AccessModeInline]


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
    list_display = ('name', 'dataset_family', 'description')


admin.site.register(Database, DatabaseAdmin)
admin.site.register(DatasetFamily, DatasetFamilyAdmin)
admin.site.register(AccessAchievement, AccessAchievementAdmin)
admin.site.register(Consumer, ConsumerAdmin)
admin.site.register(AccessModeType, AccessModeTypeAdmin)
admin.site.register(AccessModeAnonymization, AccessModeAnonymizationAdmin)
admin.site.register(AccessModeResearchField, AccessModeResearchFieldAdmin)
admin.site.register(AccessMode, AccessModeAdmin)

admin.site.site_header = 'IDA/IRMA/DSM administration'
