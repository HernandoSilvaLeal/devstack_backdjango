from django.db import models
from apps.base.models import BaseModel

# Parte 0: Importaciones necesarias para las relaciones entre modelos.
# Parte 1: Model ---> El nombre del modelo (Tabla o Entidad)
# Parte 2: BaseModel ---> Modelo que hereda los campos del modelo base (Pk y demas)
# Parte 3: Campos ---> Los fijados en el modelo MER (Atributos)
# Parte 4: Clase Meta + Orderin --->  Definicion en los metadatos (Nombre del modelo)
# Parte 5: Funcion __str__ ---> Representacion en Unicode
# Parte 6: Funciones adicionales @

# 3.1 AssetsModel
class AssetsModel(BaseModel):

    
    class Meta:
        verbose_name = _("AssetsModel")
        verbose_name_plural = _("AssetsModels")

    def __str__(self):
        return self.name



# 3.2 PhysicalassetsModel
class PhysicalassetsModel(BaseModel):

    

    class Meta:
        verbose_name = _("PhysicalassetsModel")
        verbose_name_plural = _("PhysicalassetsModels")

    def __str__(self):
        return self.name


# 3.3 InformationassetsModel
class InformationassetsModel(BaseModel):

    

    class Meta:
        verbose_name = _("InformationassetsModel")
        verbose_name_plural = _("InformationassetsModels")

    def __str__(self):
        return self.name



# 3.4 ServiceassetsModel
class ServiceassetsModel(BaseModel):

    

    class Meta:
        verbose_name = _("ServiceassetsModel")
        verbose_name_plural = _("ServiceassetsModels")

    def __str__(self):
        return self.name


# 3.5 PersonalassetsModel
class PersonalassetsModel(BaseModel):

    

    class Meta:
        verbose_name = _("PersonalassetsModel")
        verbose_name_plural = _("PersonalassetsModels")

    def __str__(self):
        return self.name


