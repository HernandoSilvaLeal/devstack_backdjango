#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os                                                                               # Libreria para poder usar funcionalidades del sistema operativo
import sys                                                                              # Libreria que permite ejecutar el interprete de python


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devstackcore.settings.local') 
    try:
        from django.core.management import execute_from_command_line                    # Importacion de Django con su administrador para utilizar todo el framework
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "               # Error que arroja el programa cuando no encuentra django, en venv esta desactivado o similares.
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)                                                  # Lista de argumentos que se pasan al interprete dentro de toda la ejecucion del programa


if __name__ == '__main__':                                                               # Si este modulo fue importado, disponibiliza las funciones sin ejecutar scripts internos.
    main()                                                                               # Si este modulo fue ejecutado directamente, lee las funciones y ejecuta todos los scripts internos.
