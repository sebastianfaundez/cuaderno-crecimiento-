from django.db import models
from django.contrib.auth.models import User
from .choices import sexos
from .choices import fuentes_datos
from datetime import date

# Create your models here.
class PerfilMenor(models.Model):
    
    usuario_principal = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    nombres = models.CharField(max_length=50, verbose_name="Nombres")
    apellido_paterno = models.CharField(max_length=20, verbose_name="Apellido Paterno")
    apellido_materno = models.CharField(max_length=20, verbose_name="Apellido Materno")
    fecha_nacimiento =models.DateField()
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    observaciones = models.CharField(max_length=200, blank=True, null=True, default=None)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    
    #calcula edad actual
    @property
    def edad_actual(self):
        """
        Calcular edad actual basado en fecha de nacimiento
        :return: int edad
        """
        if self.fecha_nacimiento:
            # Obtener fecha de hoy
            today = date.today()
            # Calcular Edad
            age = today.year - self.fecha_nacimiento.year - (
                    (today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
            return age

        # Si no tiene fecha su edad es 0
        return 0
    
    
    
    
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
    
    
    # Tallas edad niñas desde nacimiento a 5 años zscores
class TallaEdadNinasNac5AnosZscores(models.Model):
    anos_meses = models.CharField(max_length=5, primary_key=True)
    meses = models.IntegerField(blank=True, null=True)
    menos2de = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    menos1de = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    mediana = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    mas1de = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    mas2de = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'talla_edad_ninas_nac5anos_zscores'

class TallaEdadNinosNac5AnosZscores(models.Model):
    anos_meses = models.CharField(max_length=5, primary_key=True)
    meses = models.IntegerField(blank=True, null=True)
    menos2de = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    menos1de = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    mediana = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    mas1de = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    mas2de = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'talla_edad_ninos_nac5anos_zscores'


class PesoEdadNinasNac5AnosZscores(models.Model):
    anos_meses = models.CharField(max_length=5, primary_key=True)
    meses = models.IntegerField(blank=True, null=True)
    menos2de = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    menos1de = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    mediana = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    mas1de = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    mas2de = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'peso_edad_ninas_nac5anos_zscores'


class PesoEdadNinosNac5AnosZscores(models.Model):
    anos_meses = models.CharField(max_length=5, primary_key=True)
    meses = models.IntegerField(blank=True, null=True)
    menos2de = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    menos1de = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    mediana = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    mas1de = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    mas2de = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'peso_edad_ninos_nac5anos_zscores'