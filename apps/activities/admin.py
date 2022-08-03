from django.contrib import admin
from apps.activities.api import models

# Paso #1 - Importar los modelos   from . import models
# Paso #2 - Registrar los modelos  admin.site.register(models.Category)
# Paso #3 - Clase para render con atributo list_display list_display = ('slug', 'author')

admin.site.register(models.ActivitiesModel)
admin.site.register(models.ControlsModel)
admin.site.register(models.RisksModel)
admin.site.register(models.ThreatsModel)
admin.site.register(models.ResultsModel)

class ActivityAdmin(admin.ActivitiesModel):
    list_display = ('name', 'type', 'referenceISO', 'description', 'area', 'Creacion')
class ControlsAdmin(admin.ControlsModel):
    list_display = ('title', 'notes', 'imageUpload', 'check', 'corrected', 'managed', 'category_activity')
class RisksAdmin(admin.RisksModel):
    list_display = ('title', 'notes', 'imageUpload', 'check', 'corrected', 'managed', 'category_activity')
class ThreatsAdmin(admin.ThreatsModel):
    list_display = ('title', 'notes', 'imageUpload', 'check', 'corrected', 'managed', 'category_activity')
class ResultsAdmin(admin.ResultsModel):
    list_display = ('title', 'notes', 'imageUpload', 'check', 'corrected', 'managed', 'category_activity')
    
# ActivitiesAdmin
# ControlsAdmin
# RisksAdmin
# ThreatsAdmin
# ResultsAdmin

# ActivitiesModel
# ControlsModel
# RisksModel
# ThreatsModel
# ResultsModel

