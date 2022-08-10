from django.contrib import admin
from apps.projects.api import models

# Paso #1 - Importar los modelos   from . import models
# Paso #2 - Registrar los modelos  admin.site.register(models.Category)
# Paso #3 - Clase para render con atributo list_display list_display = ('slug', 'author')

admin.site.register(models.ProjectsModel)
admin.site.register(models.CompaniesModel)
admin.site.register(models.StagesModel)
admin.site.register(models.AreasModel)

class ProjectsAdmin(models.ProjectsModel):
    list_display = (
        'nameproject', 
        'budget', 
        'objetives', 
        'number_of_stages', 
        'dateinitial', 
        'datecompletion', 
        'current_month', 
        'adminproject', 
        'auditorproject', 
        'leaderproject', 
        'percentage_of_progress')
class CompaniesAdmin(models.CompaniesModel):
    list_display = (
        'comercial_name', 
        'nit', 
        'slogan', 
        'logo', 
        'number_of_areas', 
        'amount_of_assets', 
        'project', 
        'notes')
class StagesAdmin(models.StagesModel):
    list_display = (
        'comercial_name', 
        'number_stage', 
        'type', 
        'date_dalivery_stage', 
    )
class AreasAdmin(models.AreasModel):
    list_display = (
        'name_area', 
        'leader', 
        'company', 
        'notes', 
    )
    
# ProjectsAdmin
# CompaniesAdmin
# StagesAdmin
# AreasAdmin

# ProjectsModel
# CompaniesModel
# StagesModel
# AreasModel
