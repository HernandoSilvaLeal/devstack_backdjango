from django.db import models
from apps.base.models import BaseModel
from apps.projects.api.models import ProjectsModel, CompaniesModel

# Parte 0: Importaciones necesarias para las relaciones entre modelos.
# Parte 1: Model ---> El nombre del modelo (Tabla o Entidad)
# Parte 2: BaseModel ---> Modelo que hereda los campos del modelo base (Pk y demas)
# Parte 3: Campos ---> Los fijados en el modelo MER (Atributos)
# Parte 4: Clase Meta + Orderin --->  Definicion en los metadatos (Nombre del modelo)
# Parte 5: Funcion __str__ ---> Representacion en Unicode
# Parte 6: Funciones adicionales @

# 5.1 ProgressreportModel
class ProgressreportModel(BaseModel):

    project = models.ForeignKey(ProjectsModel, verbose_name=_(""), on_delete=models.CASCADE)
    company = models.ForeignKey(CompaniesModel, verbose_name=_(""), on_delete=models.CASCADE)
    dateinitial = models.DateField('Fecha Inicio de Proyecto', auto_now=False, auto_now_add=False) # Revisar relacion foranea a un campo especifico.
    datecompletion = models.DateField('Fecha Inicio de Proyecto', auto_now=False, auto_now_add=False) # Revisar relacion foranea a un campo especifico.
    adminproject = models.CharField('Responsable', max_length=50) # Revisar construccion de relacion con users
    auditorproject =  models.CharField('Responsable', max_length=50) # Revisar construccion de relacion con users
    leaderproject =  models.CharField('Responsable', max_length=50) # Revisar construccion de relacion con users
    notes = models.CharField('Notas', max_length=200)
    # Falta mas analisis en el informe.

    class Meta:
        ordering = ['-id']                                                                              # Orden descendente o ascendente        
        verbose_name = 'ProgressreportModel'
        verbose_name_plural = 'ProgressreportModels'

    def __str__(self):
        return self.name


# 5.2 IndicatorsModel
class IndicatorsModel(ProgressreportModel):

    nameIndicator = models.CharField('Nombre del Informe', max_length=50)
    stages_completed = models.DecimalField('Etapas Completadas', max_digits=5, decimal_places=2)
    activities_completed = models.DecimalField('Actividades Completadas', max_digits=5, decimal_places=2)
    controls_completed = models.DecimalField('Controles Completadas', max_digits=5, decimal_places=2)
    risks_completed = models.DecimalField('Riesgos Completadas', max_digits=5, decimal_places=2)
    threats_completed = models.DecimalField('Amenazas Completadas', max_digits=5, decimal_places=2)
    results_completed = models.DecimalField('Resultados Completadas', max_digits=5, decimal_places=2)

    class Meta:
        ordering = ['-id']                                                                              # Orden descendente o ascendente        
        verbose_name = 'IndicatorsModel'
        verbose_name_plural = '"IndicatorsModels'

    def __str__(self):
        return self.name



# 5.3 CalendarModel
class CalendarModel(BaseModel):

    date_dalivery_stage_1 = models.DateField('Fecha Entrega Etapa 1', auto_now=False, auto_now_add=True)
    date_dalivery_stage_2 = models.DateField('Fecha Entrega Etapa 2', auto_now=False, auto_now_add=True)
    date_dalivery_stage_3 = models.DateField('Fecha Entrega Etapa 3', auto_now=False, auto_now_add=True)
    date_dalivery_stage_4 = models.DateField('Fecha Entrega Etapa 4', auto_now=False, auto_now_add=True)
    date_dalivery_stage_5 = models.DateField('Fecha Entrega Etapa 5', auto_now=False, auto_now_add=True)
    date_dalivery_stage_6 = models.DateField('Fecha Entrega Etapa 6', auto_now=False, auto_now_add=True)
    date_dalivery_stage_7 = models.DateField('Fecha Entrega Etapa 7', auto_now=False, auto_now_add=True)
    date_dalivery_stage_8 = models.DateField('Fecha Entrega Etapa 8', auto_now=False, auto_now_add=True)
    date_dalivery_stage_9 = models.DateField('Fecha Entrega Etapa 9', auto_now=False, auto_now_add=True)
    date_dalivery_stage_10 = models.DateField('Fecha Entrega Etapa 10', auto_now=False, auto_now_add=True)
    date_dalivery_stage_11 = models.DateField('Fecha Entrega Etapa 11', auto_now=False, auto_now_add=True)
    date_dalivery_stage_12 = models.DateField('Fecha Entrega Etapa 11', auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ['-id']                                                                              # Orden descendente o ascendente        
        verbose_name = 'CalendarModel'
        verbose_name_plural = 'CalendarModels'

    def __str__(self):
        return self.name




