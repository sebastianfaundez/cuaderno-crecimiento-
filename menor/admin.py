from django.contrib import admin
# se importan los modelos via nombre de sus clases en el archivo menor\models.py
from .models import PerfilMenor 
from .models import MedicionCrecimiento 


class MedicionCrecimientoAdmin(admin.ModelAdmin):
    list_display = ('id_menor_display', 'nombre_menor_display', 'fecha_medicion', 'fuente_dato' ,'edad_anos', 'edad_meses', 'id_medicion_display')

    
    # This method creates the data for the new column
    @admin.display(description='ID Menor') # Sets the header to "Full Name"
    def id_menor_display(self, obj):
        return f"{obj.perfil_id}"
    
    # This method creates the data for the new column
    @admin.display(description='Nombre') # Sets the header to "Full Name"
    def nombre_menor_display(self, obj):
        return f"{obj.perfil}"
    
    # This method creates the data for the new column
    @admin.display(description='ID Medición') 
    def id_medicion_display(self, obj):
        return f"{obj.id}"


    ordering = ('perfil',)

      # Adds a filter sidebar for these fields
    #list_filter = ('category', 'release_date', 'in_stock')
      # Adds a filter sidebar for these fields
    list_filter = ('perfil',)

class PerfilMenorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_completo', 'fecha_nacimiento', 'sexo', 'usuario_principal')
    
admin.site.register(MedicionCrecimiento, MedicionCrecimientoAdmin)
admin.site.register(PerfilMenor, PerfilMenorAdmin)