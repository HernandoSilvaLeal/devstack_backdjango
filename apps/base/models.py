from django.db import models
from django.utils import timezone
# from simple_history.models import HistoricalRecords

# Parte 0: Importaciones necesarias para las relaciones entre modelos.
# Parte 1: Model ---> El nombre del modelo (Tabla o Entidad)
# Parte 2: BaseModel ---> Modelo que hereda los campos del modelo base (Pk y demas)
# Parte 3: Campos ---> Los fijados en el modelo MER (Atributos)
# Parte 4: Clase Meta + Orderin --->  Definicion en los metadatos (Nombre del modelo)
# Parte 5: Funcion __str__ ---> Representacion en Unicode
# Parte 6: Funciones adicionales @
# Parte 7: Funcion get_absolute_url, no se usan porque es DRF y no D = https://stackoverflow.com/questions/43179875/when-to-use-django-get-absolute-url-method
# Parte 8: Herencia entre modelos --> https://pywombat.com/articles/herencias-modelos-django

class BaseModel(models.Model):
    """Model definition for BaseModel."""

    # class CustomNndObjects(models.Manager):
    #     def get_queryset(self):
    #         return super().get_queryset().filter()

    # TODO: Define fields here
    id = models.AutoField(primary_key = True)
    state = models.BooleanField('Estado',default = True)
    created_date = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=False, default='2022-08-05')
    modified_date = models.DateField('Fecha de Modificación', auto_now=True, auto_now_add=False)
    deleted_date = models.DateField('Fecha de Eliminación', auto_now=True, auto_now_add=False)
    objects = models.Manager()  # default manager
    # historical = HistoricalRecords(user_model="users.User", inherit=True)
    # postobjects = CustomNndObjects()  # custom manager

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for BaseModel."""
        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Base'

# Boolean

# Interger
# Decimal

# Image 

# JSONfield

# Date 

# CharField
# TextField 

# URLField 

# ForeignKey
# ManyToManyField 
# OneToOneField¶