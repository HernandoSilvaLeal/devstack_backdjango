from django.db import models
from apps.base.models import BaseModel
from apps.projects.api.models import AreasModel

# Parte 0: Importaciones necesarias para las relaciones entre modelos.
# Parte 1: Model ---> El nombre del modelo (Tabla o Entidad)
# Parte 2: BaseModel ---> Modelo que hereda los campos del modelo base (Pk y demas)
# Parte 3: Campos ---> Los fijados en el modelo MER (Atributos)
# Parte 4: Clase Meta + Orderin --->  Definicion en los metadatos (Nombre del modelo)
# Parte 5: Funcion __str__ ---> Representacion en Unicode
# Parte 6: Funciones adicionales @


# 4.1 ActivitiesModel
class ActivitiesModel(BaseModel):

    options = (
        ('control', 'Control'),
        ('riesgo', 'Riesgo'),
        ('amenaza', 'Amenaza'),
        ('resultado', 'Resultado'),
    )
    
    name = models.CharField("Nombre de la Actividad", max_length=50, unique=True, blank=False, null=False)
    type = models.CharField('Tipo de Actividad', max_length=20, choices=options, default='Ninguna')
    referenceISO = models.CharField("Referencia a la Norma", max_length=50)
    description = models.TextField("Descripcion General", max_length=200, blank=False, null=False)
    area = models.ForeignKey(AreasModel, verbose_name="Area de la Empresa", on_delete=models.CASCADE)
    Creacion = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-id']                                                                              # Orden descendente o ascendente        
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'

    def __str__(self):
        return self.name


# 4.2 ControlsModel
class ControlsModel(ActivitiesModel):

    title = models.CharField('Titulo del Control', max_length=50)
    notes = models.CharField('Notas', max_length=200)
    imageUpload = models.ImageField('Imagen Adjunta', upload_to='activities/', blank=True, null=True)
    check = models.BooleanField(default = False)
    corrected = models.BooleanField(default = False)
    managed = models.BooleanField(default = False)
    category_activity = models.ForeignKey(ActivitiesModel, on_delete=models.CASCADE, verbose_name='Categoria de Actividad', null=True) # default=1

    class Meta:
        ordering = ['-id']                                                                              # Orden descendente o ascendente        
        verbose_name = 'ControlsModel'
        verbose_name_plural = 'ControlsModels'

    def __str__(self):
        return self.name


# 4.3 RisksModel
class RisksModel(ActivitiesModel):

    title = models.CharField('Titulo del Riesgo', max_length=50)
    notes = models.CharField('Notas', max_length=200)
    imageUpload = models.ImageField('Imagen Adjunta', upload_to='activities/', blank=True, null=True)
    check = models.BooleanField(default = False)
    corrected = models.BooleanField(default = False)
    managed = models.BooleanField(default = False)
    category_activity = models.ForeignKey(ActivitiesModel, on_delete=models.CASCADE, verbose_name='Categoria de Actividad', null=True)

    class Meta:
        ordering = ['-id']                                                                              # Orden descendente o ascendente        
        verbose_name = 'RisksModel'
        verbose_name_plural = 'RisksModels'

    def __str__(self):
        return self.name


# 4.4 ThreatsModel
class ThreatsModel(ActivitiesModel):

    title = models.CharField('Titulo del Amenaza', max_length=50)
    notes = models.CharField('Notas', max_length=200)
    imageUpload = models.ImageField('Imagen Adjunta', upload_to='activities/', blank=True, null=True)
    check = models.BooleanField(default = False)
    corrected = models.BooleanField(default = False)
    managed = models.BooleanField(default = False)
    category_activity = models.ForeignKey(ActivitiesModel, on_delete=models.CASCADE, verbose_name='Categoria de Actividad', null=True)

    class Meta:
        ordering = ['-id']                                                                              # Orden descendente o ascendente              
        verbose_name = 'ThreatsModel'
        verbose_name_plural = 'ThreatsModels'

    def __str__(self):
        return self.name


# 4.5 ResultsModel
class ResultsModel(ActivitiesModel):

    title = models.CharField('Titulo del Resultado', max_length=50)
    notes = models.CharField('Notas', max_length=200)
    imageUpload = models.ImageField('Imagen Adjunta', upload_to='activities/', blank=True, null=True)
    check = models.BooleanField(default = False)
    corrected = models.BooleanField(default = False)
    managed = models.BooleanField(default = False)
    category_activity = models.ForeignKey(ActivitiesModel, on_delete=models.CASCADE, verbose_name='Categoria de Actividad', null=True)

    class Meta:
        ordering = ['-id']                                                                              # Orden descendente o ascendente        
        verbose_name = 'ResultsModel'
        verbose_name_plural = 'ResultsModels'

    def __str__(self):
        return self.name

