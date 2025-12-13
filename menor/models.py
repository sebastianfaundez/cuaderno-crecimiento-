from django.db import models
from django.contrib.auth.models import User
#from cuenta.models import Perfil
from .choices import sexos
from .choices import fuentes_datos

# Create your models here.
class PerfilMenor(models.Model):
    
    usuario_principal = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    nombres = models.CharField(max_length=50, verbose_name="Nombres")
    apellido_paterno = models.CharField(max_length=20, verbose_name="Apellido Paterno")
    apellido_materno = models.CharField(max_length=20, verbose_name="Apellido Materno")
    fecha_nacimiento =models.DateField()
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    observaciones = models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def nombre_completo(self):
        return "{} {}, {}".format(self.apellido_paterno, self.apellido_materno, self.nombres)
     
    def __str__(self):
     return self.nombre_completo() 
    
    class Meta:
        db_table= "perfil_menor"
        verbose_name = "Perfil de Menor"
        verbose_name_plural = "Perfiles de Menores"
        ordering = ['apellido_paterno', '-apellido_materno']   
   
# modelo que almacena las mediciones registradas de los menores
# el campo perfil (perfil_id en la tabla) es el ID del menor (clave primaria) en la tabla perfil_menor 
class MedicionCrecimiento(models.Model):
    perfil = models.ForeignKey(PerfilMenor, on_delete=models.CASCADE, default=None)
    fecha_medicion = models.DateField(blank=False, default=None)
    edad_anos = models.IntegerField(blank=False, default=None)
    edad_meses = models.IntegerField(blank=False, default=None)
    peso = models.FloatField(null=True, blank=True, default=None)
    talla = models.FloatField(null=True, blank=True, default=None)
    imc = models.FloatField(blank=True, null=True)
    perimetro_cefalico = models.FloatField(blank=True, null=True)
    perimetro_cintura = models.FloatField(blank=True, null=True)
    fuente_dato = models.CharField(max_length=2, choices=fuentes_datos, blank=False)
    observaciones_medicas = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table= "medicion_crecimiento"
        verbose_name = "Medicion del Menor"
        verbose_name_plural = "Mediciones de Menores"

    def __str__(self): 
        #return self.id
        return str(self.id)