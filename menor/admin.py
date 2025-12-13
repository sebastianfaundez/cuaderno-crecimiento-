from django.contrib import admin
# se importan los modelos via nombre de sus clases en el archivo menor\models.py
from .models import PerfilMenor 
from .models import MedicionCrecimiento 
# Register your models here.
admin.site.register(PerfilMenor)
admin.site.register(MedicionCrecimiento)
