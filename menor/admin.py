from django.contrib import admin
# se importan los modelos via nombre de sus clases en el archivo menor\models.py
from .models import PerfilMenor 
from .models import MedicionCrecimiento 


class MedicionCrecimientoAdmin(admin.ModelAdmin):
    list_display = ('id', 'perfil',  'fecha_medicion', 'fuente_dato' ,'edad_anos', 'edad_meses')
    ordering = ('perfil',)

class PerfilMenorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_completo', 'fecha_nacimiento', 'sexo', 'usuario_principal')
    
admin.site.register(MedicionCrecimiento, MedicionCrecimientoAdmin)
admin.site.register(PerfilMenor, PerfilMenorAdmin)