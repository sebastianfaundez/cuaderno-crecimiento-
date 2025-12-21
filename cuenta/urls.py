from django.urls import path
from .views import login_view, control_view
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', login_view, name='login'),
    path('login/', login_view, name='login'),
    path('panel_de_control/', control_view, name='panel_de_control'),
    path('registro/', views.registro, name='registro'),
    path('registro_secundario/', views.registroUsuarioSecundario, name='registro_secundario'),
    path('usuarios_secundarios/', views.usuarios_secundarios_view, name='usuarios_secundarios'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
