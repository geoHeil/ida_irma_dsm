from django.contrib import admin

from .models import Consumer, Database, DatasetFamily

admin.site.register(Consumer)
admin.site.register(Database)
admin.site.register(DatasetFamily)

admin.site.site_header = 'IDA/IRMA/DSM administration'
