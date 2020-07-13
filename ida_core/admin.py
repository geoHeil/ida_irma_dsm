from django.contrib import admin

from .models import Consumer

admin.site.register(Consumer)

admin.site.site_header = 'IDA/IRMA/DSM administration'
