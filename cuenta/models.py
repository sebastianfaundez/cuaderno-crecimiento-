from django.db import models

# Create your models here.
from django.contrib.auth.models import User 

class Perfil(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE)
    telefono =models.CharField(max_length=10)
    fecha_nacimiento =models.DateField()

    def __str__(self):
        return self.user.username