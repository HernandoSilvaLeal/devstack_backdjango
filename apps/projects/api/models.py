from django.db import models
from apps.base.models import BaseModel

# Parte 0: Importaciones necesarias para las relaciones entre modelos.
# Parte 1: Model ---> El nombre del modelo (Tabla o Entidad)
# Parte 2: BaseModel ---> Modelo que hereda los campos del modelo base (Pk y demas)
# Parte 3: Campos ---> Los fijados en el modelo MER (Atributos)
# Parte 4: Clase Meta + Orderin --->  Definicion en los metadatos (Nombre del modelo)
# Parte 5: Funcion __str__ ---> Representacion en Unicode
# Parte 6: Funciones adicionales @

# 2.1 ProjectsModel
class ProjectsModel(BaseModel):

    nameproject = models.CharField("Nombre del Proyecto", max_length=50, unique=True, blank=False, null=False)
    budget = models.IntegerField('Presupuesto en pesos')
    objetives = models.TextField('Objetivos del Proyecto')
    number_of_stages = models.IntegerField('Cantidad de Etapas')
    dateinitial = models.DateField('Fecha Inicio de Proyecto', auto_now=False, auto_now_add=False) # Revisar relacion foranea a un campo especifico modelo metrics
    datecompletion = models.DateField('Fecha Inicio de Proyecto', auto_now=False, auto_now_add=False) # Revisar relacion foranea a un campo especifico. modelo metrics
    current_month = models.IntegerField('Mes en curso del prouecto')
    adminproject = models.CharField('Responsable', max_length=50) # Revisar construccion de relacion con users
    auditorproject =  models.CharField('Responsable', max_length=50) # Revisar construccion de relacion con users
    leaderproject =  models.CharField('Responsable', max_length=50) # Revisar construccion de relacion con users
    percentage_of_progress = models.IntegerField('Porcentaje de Avance') # Revisar como calcular campo, y como ponerlo en bd como %

    class Meta:
        ordering = ['-id']                                                                              # Orden descendente o ascendente        
        verbose_name = 'ProjectsModel'
        verbose_name_plural = 'ProjectsModels'

    def __str__(self):
        return self.name


# 2.2 CompaniesModel
class CompaniesModel(BaseModel):

    comercial_name = models.CharField('Razon Social', max_length=50)
    nit = models.CharField('Nit', max_length=11)
    slogan = models.CharField('Slogan', max_length=100)
    logo = models.ImageField('Logotipo', upload_to='projects/', blank=True, null=True)
    number_of_areas = models.IntegerField('Cantidad de Areas')
    amount_of_assets = models.IntegerField('Cantidad de Activos')
    project = models.ForeignKey(ProjectsModel.nameproject, verbose_name=_(""), on_delete=models.CASCADE)
    notes = models.CharField('Notas', max_length=200)

    class Meta:
        ordering = ['-id']                                                                              # Orden descendente o ascendente        
        verbose_name = 'CompaniesModel'
        verbose_name_plural = 'CompaniesModels'

    def __str__(self):
        return self.name



# 2.3 StagesModel
class StagesModel(BaseModel):
    
    options = (
        ('primera', 'Primera'),
        ('segunda', 'Segunda'),
        ('tercera', 'Tercera'),
        ('cuarta', 'Cuarta'),
        ('quinta', 'Quinta'),
        ('sexta', 'Sexta'),
        ('septima', 'Septima'),
        ('octava', 'Octava'),
        ('novena', 'Novena'),
        ('decima', 'Decima'),
        ('undecima', 'Undecima'),
        ('duodecima', 'Duodecima'),
    )

    comercial_name = models.CharField('Nombre de la Etapa', max_length=50)
    number_stage = models.IntegerField('Cantidad de Etapas', choices=options, default = 1)
    type = models.CharField('Tipo de Actividad', max_length=20, choices=options, default='Ninguna')
    date_dalivery_stage = models.DateField('Fecha Entrega Etapa 1', auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ['-id']                                                                              # Orden descendente o ascendente        
        verbose_name = 'StagesModel'
        verbose_name_plural = 'StagesModels'

    def __str__(self):
        return self.name


# 2.4 AreasModel
class AreasModel(BaseModel):

    name_area = models.CharField('Nombre del Area', max_length=50)
    leader = models.ForeignKey(ProjectsModel.leaderproject, verbose_name=_(""), on_delete=models.CASCADE)
    company = models.ForeignKey(CompaniesModel.comercial_name, verbose_name=_(""), on_delete=models.CASCADE)
    notes = models.CharField('Notas', max_length=200)

    class Meta:
        ordering = ['-id']                                                                              # Orden descendente o ascendente        
        verbose_name = 'AreasModel'
        verbose_name_plural = 'AreasModels'

    def __str__(self):
        return self.name



