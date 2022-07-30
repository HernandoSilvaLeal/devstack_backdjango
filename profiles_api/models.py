from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):                  # Manager para Perfiles de Usuario

    def create_user(self, email, name, password=None):      # Esto nos permite crear usuarios
        if not email:
            raise ValueError('Usuario debe tener un Email')
        
        email = self.normalize_email(email)                 # Convertir todo el email a minuscular
        user = self.model(email=email, name=name)           # Objeto de usuario definido

        user.set_password(password)                         # El usuario necesita una contraseña
        user.save(using=self._db)                           # Me aseguro que el password este en hash

        return user
    
    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True 
        user.is_staff = True 
        user.save(using=self._db)


class UserProfile(AbstractBaseUser,PermissionsMixin):       # Modelo Base de Datos para Usuarios en el Sistema
    namep=models.CharField(max_length=255)
    emailp=models.EmailField(max_length=255,unique=True)
    is_activep=models.BooleanField(default=True)
    is_staffp=models.BooleanField(default=False)

    objectsp = UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    def get_full_name(self):                                # Obtener Nombre Completo del Usuario
        return self.namep

    def get_short_name(self):                               # Obtener nombre corto
        return self.namep

    def _str_(self):                                        # Retornar Codena Representando Nuestro Usuario 
        return self.emailp


