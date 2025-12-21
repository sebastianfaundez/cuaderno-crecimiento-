from django import forms 
from . import models 
from django.core.exceptions import ValidationError 


class CrearPerfilMenorForm(forms.ModelForm):

    class Meta:
        model = models.PerfilMenor 
        fields=['nombres', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento', 'sexo', 'observaciones']

        widgets = {
            'nombres': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_materno': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class':'form-control', 'type':'date'}) ,   
            'sexo': forms.Select(attrs={'class':'form-control'}) ,     
            'observaciones': forms.Textarea(attrs={'class':'form-control'}),                                                      
            }
    
    


class RegistrarMedicionForm(forms.ModelForm):
    
    class Meta:
       model = models.MedicionCrecimiento
       #fields=['fecha_medicion', 'fuente_dato', 'edad_anos', 'edad_meses', 'talla', 'peso', 'imc', 'perimetro_cefalico', 'perimetro_cintura', 'observaciones_medicas'] 
       fields=['fecha_medicion', 'fuente_dato', 'edad_anos', 'edad_meses', 'talla', 'peso', 'imc', 'perimetro_cefalico', 'observaciones_medicas'] 

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
         'observaciones_medicas': forms.Textarea(attrs={'cols': '150', 'rows': '4'}),
         #'fecha_medicion': forms.DateInput(format='%d/%m/%Y'),
         'fecha_medicion': forms.DateInput(format='%d/%m/%Y', attrs={
             'placeholder': 'Ej: 01/08/2012'
         }),
       
       
       }

       
     
       
    
    
       
     
       
    def clean(self):
           print('linea 40 forms.py')
           cleaned_data = super().clean()
           input_peso = cleaned_data.get('peso')
           input_talla = cleaned_data.get('talla')
        
           if not input_peso and not input_talla:
                print('linea 46 forms.py')
                raise ValidationError("Debe especificar Talla o Peso (al menos uno de esos dos valores).")
           return cleaned_data       

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control rounded-5 me-2'
            self.fields['fecha_medicion'].input_formats = ['%d-%m-%Y', '%d/%m/%Y']
            
