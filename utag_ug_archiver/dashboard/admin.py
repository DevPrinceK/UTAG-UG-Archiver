from django.contrib import admin

admin.site.site_header = "UTAG-UG Archiver Admin"
admin.site.site_title = "UTAG-UG Archiver Admin Portal"
admin.site.index_title = "Welcome to UTAG-UG Archiver Portal"

# Register your models here.
from .models import Event, News, ExecutivePosition, Executive, File, Document
admin.site.register(Event)
admin.site.register(News)
admin.site.register(ExecutivePosition)
admin.site.register(Executive)
admin.site.register(File)
admin.site.register(Document)

