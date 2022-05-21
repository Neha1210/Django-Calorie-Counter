from django.contrib import admin
from import_export.admin import *
from .models import *

# Register your models here.
admin.site.register(getfoodinfo)

class foodcalAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['foodname',  'foodcal']


admin.site.register(foodcal, foodcalAdmin)