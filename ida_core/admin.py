from django.contrib import admin

from .models import Database, DatasetFamily, AccessAchievement, Consumer, AccessModeCategory, AccessMode

admin.site.register(Database)
admin.site.register(DatasetFamily)
admin.site.register(AccessAchievement)
admin.site.register(Consumer)
admin.site.register(AccessModeCategory)
admin.site.register(AccessMode)

admin.site.site_header = 'IDA/IRMA/DSM administration'
