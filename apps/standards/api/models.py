from django.db import models
from apps.base.models import BaseModel

# Parte 0: Importaciones necesarias para las relaciones entre modelos.
# Parte 1: Model ---> El nombre del modelo (Tabla o Entidad)
# Parte 2: BaseModel ---> Modelo que hereda los campos del modelo base (Pk y demas)
# Parte 3: Campos ---> Los fijados en el modelo MER (Atributos)
# Parte 4: Clase Meta + Orderin --->  Definicion en los metadatos (Nombre del modelo)
# Parte 5: Funcion __str__ ---> Representacion en Unicode
# Parte 6: Funciones adicionales @

# 7.1 StandardsModel
class StandardsModel(BaseModel):

    

    class Meta:
        ordering = ['-id']                                                                              # Orden descendente o ascendente        
        verbose_name = _("StandardsModel")
        verbose_name_plural = _("StandardsModels")

    def __str__(self):
        return self.name



# 7.2 ChaptersModel
class ChaptersModel(BaseModel):

    
    class Meta:
        ordering = ['-id']                                                                              # Orden descendente o ascendente        
        verbose_name = _("ChaptersModel")
        verbose_name_plural = _("ChaptersModels")

    def __str__(self):
        return self.name



# 7.3 ArticlesModel
class ArticlesModel(BaseModel):

    

    class Meta:
        ordering = ['-id']                                                                              # Orden descendente o ascendente        
        verbose_name = _("ArticlesModel")
        verbose_name_plural = _("ArticlesModels")

    def __str__(self):
        return self.name



