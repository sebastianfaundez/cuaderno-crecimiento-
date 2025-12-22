from django.urls import path
#from cuenta.views import control_view
from .views import crear_perfil_menor_view
from .views import listar_perfiles_menores_view
from . import views

#app_name = 'menor'
urlpatterns = [
    path('crear_perfil_menor/', crear_perfil_menor_view, name='crear_perfil_menor'),
    path('listar_menores/', listar_perfiles_menores_view, name='listar_menores'),
    path('historico_mediciones_menor/<int:id>', views.historico_mediciones_menor_view, name='historico_mediciones_menor'),
    path('ficha_menor/<int:id>', views.ficha_menor_view, name='ficha_menor'),
    path('registrar_medicion/<int:id>', views.registrar_medicion_view, name='registrar_medicion'),
    path('reporte_simple_menor/<int:id>', views.reporte_simple_view_function, name='reporte_simple_menor'),
]
