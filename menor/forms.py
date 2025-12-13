from django import forms 
from . import models 
from django.core.exceptions import ValidationError 

class CrearPerfilMenorForm(forms.ModelForm):

    class Meta:
        model = models.PerfilMenor 
        fields=['nombres', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento', 'sexo', 'observaciones']

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class RegistrarMedicionForm(forms.ModelForm):
    
    class Meta:
       model = models.MedicionCrecimiento
       fields=['fecha_medicion', 'fuente_dato', 'edad_anos', 'edad_meses', 'talla', 'peso', 'imc', 'perimetro_cefalico', 'perimetro_cintura', 'observaciones_medicas'] 
       
       labels = {
                'fecha_medicion': "Fecha de la Medición",
                'peso': "Peso (K,gr)",
                'talla': "Talla (Cms)",
                'edad_anos': "Edad en años",
                'edad_meses': "Edad en meses",
                'imc': "IMC",
                'perimetro_cefalico': "Perímetro craneal",
            }
       
       widgets = {
        #'observaciones_medicas': forms.Textarea(attrs={'class': 'form-control'}),
        'observaciones_medicas': forms.Textarea(),
          }
       
    def clean(self):
           print('linea 35 forms.py')
           cleaned_data = super().clean()
           input_peso = cleaned_data.get('peso')
           input_talla = cleaned_data.get('talla')
        
           if not input_peso and not input_talla:
                raise ValidationError("Debe especificar Peso o Talla (al menos uno de esos valores).")
           return cleaned_data       

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            
