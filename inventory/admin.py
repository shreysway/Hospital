from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.

# admin.site.register(item)
@admin.register(Desktops)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id', )
