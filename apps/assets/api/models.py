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
        ('fisico', 'Fisico'),
        ('informatico', 'Informatico'),
        ('servicio', 'Servicio'),
        ('personal', 'Personal'),
    )
    
    options_substate = (
        ('fisico', 'Fisico'),
        ('informatico', 'Informatico'),
        ('servicio', 'Servicio'),
        ('personal', 'Personal'),
    )
    name = models.CharField("Nombre del Activo", max_length=50, unique=True, blank=False, null=False)
    type = models.CharField('Tipo del Activo', max_length=20, choices=options_type, default='Ninguna')
    appraisal = models.DecimalField('Avaluo', max_digits=5, decimal_places=2)
    description = models.TextField("Descripcion General", max_length=200, blank=False, null=False)
    company = models.ForeignKey(CompaniesModel, verbose_name=_("Empresa"), on_delete=models.CASCADE)
    location = models.CharField("Nombre del Activo", max_length=50, unique=True, blank=False, null=False)
    substate = models.CharField('Tipo del Activo', max_length=20, choices=options_substate, default='Ninguna')
    Creacion = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = _("AssetsModel")
        verbose_name_plural = _("AssetsModels")

    def __str__(self):
        return self.name



# 3.2 PhysicalassetsModel
class PhysicalassetsModel(AssetsModel):

    title = models.CharField('Titulo del Activo Fisico', max_length=50)
    notes = models.CharField('Notas', max_length=200)
    imageUpload = models.ImageField('Imagen Adjunta', upload_to='assets/', blank=True, null=True)
    delegated = models.CharField('Responsable', max_length=50)
    check = models.BooleanField(default = False)
    corrected = models.BooleanField(default = False)
    managed = models.BooleanField(default = False)
    category_assets = models.ForeignKey(AssetsModel, on_delete=models.CASCADE, verbose_name='Categoria de Activo', null=True) # default=1

    class Meta:
        verbose_name = _("PhysicalassetsModel")
        verbose_name_plural = _("PhysicalassetsModels")

    def __str__(self):
        return self.name


# 3.3 InformationassetsModel
class InformationassetsModel(AssetsModel):

    title = models.CharField('Titulo del Activo Informatico', max_length=50)
    notes = models.CharField('Notas', max_length=200)
    imageUpload = models.ImageField('Imagen Adjunta', upload_to='assets/', blank=True, null=True)
    delegated = models.CharField('Responsable', max_length=50)
    check = models.BooleanField(default = False)
    corrected = models.BooleanField(default = False)
    managed = models.BooleanField(default = False)
    category_assets = models.ForeignKey(AssetsModel, on_delete=models.CASCADE, verbose_name='Categoria de Activo', null=True) # default=1

    class Meta:
        verbose_name = _("InformationassetsModel")
        verbose_name_plural = _("InformationassetsModels")

    def __str__(self):
        return self.name



# 3.4 ServiceassetsModel
class ServiceassetsModel(AssetsModel):

    title = models.CharField('Titulo del Activo Servicio', max_length=50)
    notes = models.CharField('Notas', max_length=200)
    imageUpload = models.ImageField('Imagen Adjunta', upload_to='assets/', blank=True, null=True)
    delegated = models.CharField('Responsable', max_length=50)
    check = models.BooleanField(default = False)
    corrected = models.BooleanField(default = False)
    managed = models.BooleanField(default = False)
    category_assets = models.ForeignKey(AssetsModel, on_delete=models.CASCADE, verbose_name='Categoria de Activo', null=True) # default=1

    class Meta:
        verbose_name = _("ServiceassetsModel")
        verbose_name_plural = _("ServiceassetsModels")

    def __str__(self):
        return self.name


# 3.5 PersonalassetsModel
class PersonalassetsModel(AssetsModel):

    title = models.CharField('Titulo del Activo Personal', max_length=50)
    notes = models.CharField('Notas', max_length=200)
    imageUpload = models.ImageField('Imagen Adjunta', upload_to='assets/', blank=True, null=True)
    delegated = models.CharField('Responsable', max_length=50)
    check = models.BooleanField(default = False)
    corrected = models.BooleanField(default = False)
    managed = models.BooleanField(default = False)
    category_assets = models.ForeignKey(AssetsModel, on_delete=models.CASCADE, verbose_name='Categoria de Activo', null=True) # default=1

    class Meta:
        verbose_name = _("PersonalassetsModel")
        verbose_name_plural = _("PersonalassetsModels")

    def __str__(self):
        return self.name


