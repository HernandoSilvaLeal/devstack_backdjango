from django.contrib import admin
from apps.standards.api import models

# Paso #1 - Importar los modelos   from . import models
# Paso #2 - Registrar los modelos  admin.site.register(models.Category)
# Paso #3 - Clase para render con atributo list_display list_display = ('slug', 'author')

admin.site.register(models.StandardsModel)
admin.site.register(models.ChaptersModel)
admin.site.register(models.ArticlesModel)

class StandardsAdmin(models.StandardsModel):
    list_display = (
        'title_standard', 
        'version_standard', 
    )
class ChaptersAdmin(models.ChaptersModel):
    list_display = (
        'title_chapter', 
        'description_chapter', 
        'image_chapter', 
        'link_chapter', 
    )
class ArticlesAdmin(models.ArticlesModel):
    list_display = (
        'title_article', 
        'description_article', 
        'image_article', 
        'link_article', 
    )

# StandardsAdmin
# ChaptersAdmin
# ArticlesAdmin

# StandardsModel
# ChaptersModel
# ArticlesModel