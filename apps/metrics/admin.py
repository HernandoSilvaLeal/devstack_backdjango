from django.contrib import admin
from apps.metrics.api import models

# Paso #1 - Importar los modelos   from . import models
# Paso #2 - Registrar los modelos  admin.site.register(models.Category)
# Paso #3 - Clase para render con atributo list_display list_display = ('slug', 'author')

admin.site.register(models.ProgressreportModel)
admin.site.register(models.IndicatorsModel)
admin.site.register(models.CalendarModel)

class ProgressreportAdmin(admin.ProgressreportModel):
    list_display = (
        'project', 
        'company', 
        'dateinitial', 
        'datecompletion', 
        'adminproject', 
        'auditorproject', 
        'leaderproject', 
        'notes')
class IndicatorsAdmin(admin.IndicatorsModel):
    list_display = (
        'nameIndicator', 
        'stages_completed', 
        'activities_completed', 
        'controls_completed', 
        'risks_completed', 
        'threats_completed', 
        'results_completed')
class CalendarAdmin(admin.CalendarModel):
    list_display = (
        'name_calendar', 
        'date_delivery_stage_1', 
        'date_delivery_stage_2', 
        'date_delivery_stage_3', 
        'date_delivery_stage_4', 
        'date_delivery_stage_5', 
        'date_delivery_stage_6', 
        'date_delivery_stage_7', 
        'date_delivery_stage_8', 
        'date_delivery_stage_9', 
        'date_delivery_stage_10', 
        'date_delivery_stage_11', 
        'date_delivery_stage_12', 
    )

# ProgressreportAdmin
# IndicatorsAdmin
# CalendarAdmin

# ProgressreportModel
# IndicatorsModel
# CalendarModel