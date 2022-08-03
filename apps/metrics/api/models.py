from django.db import models
from apps.base.models import BaseModel

# Parte 0: Importaciones necesarias para las relaciones entre modelos.
# Parte 1: Model ---> El nombre del modelo (Tabla o Entidad)
# Parte 2: BaseModel ---> Modelo que hereda los campos del modelo base (Pk y demas)
# Parte 3: Campos ---> Los fijados en el modelo MER (Atributos)
# Parte 4: Clase Meta + Orderin --->  Definicion en los metadatos (Nombre del modelo)
# Parte 5: Funcion __str__ ---> Representacion en Unicode
# Parte 6: Funciones adicionales @

# 5.1 ProgressreportModel
class ProgressreportModel(BaseModel):

    

    class Meta:
        verbose_name = _("ProgressreportModel")
        verbose_name_plural = _("ProgressreportModels")

    def __str__(self):
        return self.name


# 5.2 IndicatorsModel
class IndicatorsModel(BaseModel):

    

    class Meta:
        verbose_name = _("IndicatorsModel")
        verbose_name_plural = _("IndicatorsModels")

    def __str__(self):
        return self.name



# 5.3 CalendarModel
class CalendarModel(BaseModel):

    

    class Meta:
        verbose_name = _("CalendarModel")
        verbose_name_plural = _("CalendarModels")

    def __str__(self):
        return self.name




