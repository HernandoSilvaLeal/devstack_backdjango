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

class ActivityAdmin(models.ActivitiesModel):
    list_display = ('name_activity', 'type', 'referenceISO', 'description', 'area', 'creacion')
class ControlsAdmin(models.ControlsModel):
    list_display = ('title', 'notes', 'imageUpload', 'check_verify', 'corrected', 'managed', 'category_activity')
class RisksAdmin(models.RisksModel):
    list_display = ('title', 'notes', 'imageUpload', 'check_verify', 'corrected', 'managed', 'category_activity')
class ThreatsAdmin(models.ThreatsModel):
    list_display = ('title', 'notes', 'imageUpload', 'check_verify', 'corrected', 'managed', 'category_activity')
class ResultsAdmin(models.ResultsModel):
    list_display = ('title', 'notes', 'imageUpload', 'check_verify', 'corrected', 'managed', 'category_activity')

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
