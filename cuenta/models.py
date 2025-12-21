from django.db import models

# Create your models here.
from django.contrib.auth.models import User 

class Perfil(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE)
    telefono =models.CharField(max_length=10)
    fecha_nacimiento =models.DateField()

    def __str__(self):
        return self.user.username

# Modelo de usuario secundario
class UsuarioSecundario(models.Model):
    #usuario_principal = models.ForeignKey(User, on_delete=models.CASCADE)
    usuario_principal = models.IntegerField()
    usuario_secundario = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    #usuario_secundario_id = models.IntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table= "cuenta_usuario_secundario"

    def __str__(self):
        return self.usuario_secundario