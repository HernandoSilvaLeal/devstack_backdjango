from email import charset
from django.db import models
from apps.base.models import BaseModel

# Parte 0: Importaciones necesarias para las relaciones entre modelos.
# Parte 1: Model ---> El nombre del modelo (Tabla o Entidad)
# Parte 2: BaseModel ---> Modelo que hereda los campos del modelo base (Pk y demas)
# Parte 3: Campos ---> Los fijados en el modelo MER (Atributos)
# Parte 4: Clase Meta + Orderin --->  Definicion en los metadatos (Nombre del modelo)
# Parte 5: Funcion __str__ ---> Representacion en Unicode
# Parte 6: Funciones adicionales @

# 6.1 HelpsModel
class HelpsModel(BaseModel):

    name_help = models.CharField('Nombre del Calendario', max_length=50)
    description_help = models.TextField("Descripcion General", max_length=200, blank=False, null=False)

    class Meta:
        ordering = ['-id']                                                                              # Orden descendente o ascendente        
        verbose_name = 'HelpsModel'
        verbose_name_plural = 'HelpsModels'

    def __str__(self):
        return self.name


# 6.2 ResourcecategoryModel
class ResourcecategoryModel(HelpsModel):

    options = (
        ('link', 'Link'),
        ('video', 'Video'),
        ('imagen', 'Imagen'),
        ('contacto', 'Contacto'),
        ('adjunto', 'Adjunto'),
    )

    cateogry = models.CharField('Categoria de Recursos', choices=options, max_length=50, default = 'Ninguna')

    class Meta:
        ordering = ['-id']                                                                              # Orden descendente o ascendente        
        verbose_name = 'ResourcecategoryModel'
        verbose_name_plural = 'ResourcecategoryModels'

    def __str__(self):
        return self.name


# 6.3 ResourcesModel
class ResourcesModel(ResourcecategoryModel):

    title_resource = models.CharField('Titulo del Recurso', max_length=50)
    description_resource = models.CharField('Descripcion del Recurso', max_length=200)
    image_resource = models.ImageField('Logotipo', upload_to='resources/', blank=True, null=True)
    link_resource = models.CharField(max_length=100, default='', null=True, blank=True)

    class Meta:
        ordering = ['-id']                                                                              # Orden descendente o ascendente        
        verbose_name = 'ResourcesModel'
        verbose_name_plural = 'ResourcesModels'

    def __str__(self):
        return self.name


