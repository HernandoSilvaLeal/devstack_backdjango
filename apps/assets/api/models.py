from django.db import models
from apps.base.models import BaseModel
from apps.projects.api.models import CompaniesModel

# Parte 0: Importaciones necesarias para las relaciones entre modelos.
# Parte 1: Model ---> El nombre del modelo (Tabla o Entidad)
# Parte 2: BaseModel ---> Modelo que hereda los campos del modelo base (Pk y demas)
# Parte 3: Campos ---> Los fijados en el modelo MER (Atributos)
# Parte 4: Clase Meta + Orderin --->  Definicion en los metadatos (Nombre del modelo)
# Parte 5: Funcion __str__ ---> Representacion en Unicode
# Parte 6: Funciones adicionales @

# 3.1 AssetsModel
class AssetsModel(BaseModel):

    options_type = (
        ('ninguna', 'Ninguna'),
        ('fisico', 'Fisico'),
        ('informatico', 'Informatico'),
        ('servicio', 'Servicio'),
        ('personal', 'Personal'),
    )
    
    options_substate = (                            # Se necesita mejorar el modelo conforme a la teoeria de la ISO, con ams modelos o con mejores serializers, con campos dependientes.
        ('ninguna', 'Ninguna'),
        ('sub estado a', 'Sub Estado A'),
        ('sub estado c', 'Sub Estado C'),
        ('sub estado i', 'Sub Estado I'),
        ('sub estado d', 'Sub Estado D'),
    )
    name = models.CharField("Nombre del Activo", max_length=50, unique=True, blank=False, null=False)
    type = models.CharField('Tipo del Activo', max_length=20, choices=options_type, default=1)
    appraisal = models.DecimalField('Avaluo', max_digits=15, decimal_places=2)  # Investigar formato de moneda con $ y puntos -- > DecimalField format money
    description = models.TextField("Descripcion General", max_length=200, blank=False, null=False)
    company = models.ForeignKey(CompaniesModel, verbose_name="Empresa", on_delete=models.CASCADE)
    location = models.CharField("Nombre del Activo", max_length=50, unique=True, blank=False, null=False)
    substate = models.CharField('Subestado', max_length=20, choices=options_substate, default=1)
    creacion = models.DateTimeField(auto_now_add=False)
    class Meta:
        ordering = ['-id']                                                                              # Orden descendente o ascendente        
        verbose_name = "AssetsModel"
        verbose_name_plural = "AssetsModels"

    def __str__(self):
        return self.name



# 3.2 PhysicalassetsModel
class PhysicalassetsModel(BaseModel):

    title = models.CharField('Titulo del Activo Fisico', max_length=50)
    notes = models.CharField('Notas', max_length=200)
    imageUpload = models.ImageField('Imagen Adjunta', upload_to='assets/', blank=True, null=True)
    delegated = models.CharField('Responsable', max_length=50)
    check_verify = models.BooleanField(default = False)
    corrected = models.BooleanField(default = False)
    managed = models.BooleanField(default = False)
    category_assets = models.ForeignKey(AssetsModel, on_delete=models.CASCADE, verbose_name='Categoria de Activo', null=True) # default=1

    class Meta:
        ordering = ['-id']                                                                              # Orden descendente o ascendente        
        verbose_name = 'PhysicalassetsModel'
        verbose_name_plural = 'PhysicalassetsModels'

    def __str__(self):
        return self.name


# 3.3 InformationassetsModel
class InformationassetsModel(BaseModel):

    title = models.CharField('Titulo del Activo Informatico', max_length=50)
    notes = models.CharField('Notas', max_length=200)
    imageUpload = models.ImageField('Imagen Adjunta', upload_to='assets/', blank=True, null=True)
    delegated = models.CharField('Responsable', max_length=50)
    check_verify = models.BooleanField(default = False)
    corrected = models.BooleanField(default = False)
    managed = models.BooleanField(default = False)
    category_assets = models.ForeignKey(AssetsModel, on_delete=models.CASCADE, verbose_name='Categoria de Activo', null=True) # default=1

    class Meta:
        ordering = ['-id']                                                                              # Orden descendente o ascendente        
        verbose_name = 'InformationassetsModel'
        verbose_name_plural = 'InformationassetsModels'

    def __str__(self):
        return self.name



# 3.4 ServiceassetsModel
class ServiceassetsModel(BaseModel):

    title = models.CharField('Titulo del Activo Servicio', max_length=50)
    notes = models.CharField('Notas', max_length=200)
    imageUpload = models.ImageField('Imagen Adjunta', upload_to='assets/', blank=True, null=True)
    delegated = models.CharField('Responsable', max_length=50)
    check_verify = models.BooleanField(default = False)
    corrected = models.BooleanField(default = False)
    managed = models.BooleanField(default = False)
    category_assets = models.ForeignKey(AssetsModel, on_delete=models.CASCADE, verbose_name='Categoria de Activo', null=True) # default=1

    class Meta:
        ordering = ['-id']                                                                              # Orden descendente o ascendente        
        verbose_name = 'ServiceassetsModel'
        verbose_name_plural = 'ServiceassetsModels'

    def __str__(self):
        return self.name


# 3.5 PersonalassetsModel
class PersonalassetsModel(BaseModel):

    title = models.CharField('Titulo del Activo Personal', max_length=50)
    notes = models.CharField('Notas', max_length=200)
    imageUpload = models.ImageField('Imagen Adjunta', upload_to='assets/', blank=True, null=True)
    delegated = models.CharField('Responsable', max_length=50)
    check_verify = models.BooleanField(default = False)
    corrected = models.BooleanField(default = False)
    managed = models.BooleanField(default = False)
    category_assets = models.ForeignKey(AssetsModel, on_delete=models.CASCADE, verbose_name='Categoria de Activo', null=True) # default=1

    class Meta:
        ordering = ['-id']                                                                              # Orden descendente o ascendente        
        verbose_name = 'PersonalassetsModel'
        verbose_name_plural = 'PersonalassetsModels'

    def __str__(self):
        return self.name

# Mejoras al modelo:
# Se necesitan 4 modelos mas, 1 para cada TIPO DE ACTIVO, y cada uno es para crear una lista de categorias
# Luego de crearlos, actualizo la relacion foranea del campo category_assets de cada uno de los 4 modelos.

# Luego necesito mejorar las relaciondes herencia, asserts es el padre de los 4 tipos, y los 4 tipos e el campo category son padres de sus respectivas categorias, 1 - 4 - 4
# Lo LOGICO es que yo cree el activo en 1 de los 4 TIPOS y por ende la clase padre ACTICVOS debe ser metadato = abstracta.
# AQUI --> Como actualizaste las relaciones de herencia de los 4 modelos de tiopos de activos (inform, serv, fisicos, personales) Revisa que cuando vayas a crear un activo, se diligencien los campos sumados de clase padre y 4 clases hijas.

# Añadir un campo al modelo abstracto activos --> unverified asset ---> Funciona como una maquina de estados con 4 estados de diagnostico y gestion (unverified asset, check verify, correct, management)
# Añadir 45 campos a la clase abstracta assets (Subestado A, ...c, ...i, ...d) ---> Luego cada uno con sus opstions (https://www.pmg-ssi.com/2015/03/iso-27001-los-activos-de-informacion/) 

# IMPORTANTE antes de alimentar la base de datos ((inform, serv, fisicos, personales)) se deben nutrir las bases de datos de categorias (Relacion foranea que a esta altura ya se debio configurar "category_assets")
