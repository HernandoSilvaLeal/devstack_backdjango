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

    

    class Meta:
        verbose_name = _("ProjectsModel")
        verbose_name_plural = _("ProjectsModels")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ProjectsModel_detail", kwargs={"pk": self.pk})




# 2.2 CompaniesModel
class CompaniesModel(BaseModel):

    

    class Meta:
        verbose_name = _("CompaniesModel")
        verbose_name_plural = _("CompaniesModels")

    def __str__(self):
        return self.name



# 2.3 StagesModel
class StagesModel(BaseModel):

    

    class Meta:
        verbose_name = _("StagesModel")
        verbose_name_plural = _("StagesModels")

    def __str__(self):
        return self.name


# 2.4 AreasModel
class AreasModel(BaseModel):

    

    class Meta:
        verbose_name = _("AreasModel")
        verbose_name_plural = _("AreasModels")

    def __str__(self):
        return self.name



