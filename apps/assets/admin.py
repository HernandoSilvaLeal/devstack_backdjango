from django.contrib import admin
from apps.assets.api import models

# Paso #1 - Importar los modelos   from . import models
# Paso #2 - Registrar los modelos  admin.site.register(models.Category)
# Paso #3 - Clase para render con atributo list_display list_display = ('slug', 'author')

admin.site.register(models.AssetsModel)
admin.site.register(models.PhysicalassetsModel)
admin.site.register(models.InformationassetsModel)
admin.site.register(models.ServiceassetsModel)
admin.site.register(models.PersonalassetsModel)

class AssetsAdmin(models.AssetsModel):
    list_display = ('name', 'type', 'appraisal', 'description', 'company', 'location', 'substate', 'creacion')
class PhysicalassetsAdmin(models.PhysicalassetsModel):
    list_display = ('title', 'notes', 'imageUpload', 'delegated', 'check_verify', 'corrected', 'managed', 'category_assets')
class InformationassetsAdmin(models.InformationassetsModel):
    list_display = ('title', 'notes', 'imageUpload', 'delegated', 'check_verify', 'corrected', 'managed', 'category_assets')
class ServiceassetsAdmin(models.ServiceassetsModel):
    list_display = ('title', 'notes', 'imageUpload', 'delegated', 'check_verify', 'corrected', 'managed', 'category_assets')
class PersonalassetsAdmin(models.PersonalassetsModel):
    list_display = ('title', 'notes', 'imageUpload', 'delegated', 'check_verify', 'corrected', 'managed', 'category_assets')
    
# AssetsAdmin
# PhysicalassetsAdmin
# InformationassetsAdmin
# ServiceassetsAdmin
# PersonalassetsAdmin

# AssetsModel
# PhysicalassetsModel
# InformationassetsModel
# ServiceassetsModel
# PersonalassetsModel
