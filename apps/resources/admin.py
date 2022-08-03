from django.contrib import admin
from apps.resources.api import models

# Paso #1 - Importar los modelos   from . import models
# Paso #2 - Registrar los modelos  admin.site.register(models.Category)
# Paso #3 - Clase para render con atributo list_display list_display = ('slug', 'author')

admin.site.register(models.HelpsModel)
admin.site.register(models.ResourcecategoryModel)
admin.site.register(models.ResourcesModel)

class HelpsAdmin(admin.HelpsModel):
    list_display = (
        'name_help', 
        'description', 
    )
class ResourcecategoryAdmin(admin.ResourcecategoryModel):
    list_display = (
        'cateogry', 
    )
class ResourcesAdmin(admin.ResourcesModel):
    list_display = (
        'title', 
        'description', 
        'image', 
        'link', 
    )

# HelpsAdmin
# ResourcecategoryAdmin
# ResourcesAdmin

# HelpsModel
# ResourcecategoryModel
# ResourcesModel
