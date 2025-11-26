from django import forms 
from django.contrib.auth.models import User
from .models import Perfil 

class RegistroUsuarioForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model=User 
        fields=['username', 'first_name', 'last_name', 'email']

    def clean_password2(self):
        pass1=self.cleaned_data.get('password')
        pass2=self.cleaned_data.get('password2')
        if pass1 and pass2 and pass1 != pass2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return pass2
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class PerfilForm(forms.ModelForm):

    class Meta:
        model=Perfil
        fields=['telefono', 'fecha_nacimiento']
