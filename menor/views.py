from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CrearPerfilMenorForm
from .forms import RegistrarMedicionForm
from .models import PerfilMenor
from .models import MedicionCrecimiento
from .models import TallaEdadNinasNac5AnosZscores
from .models import TallaEdadNinosNac5AnosZscores
from .models import PesoEdadNinasNac5AnosZscores
from .models import PesoEdadNinosNac5AnosZscores
from django.contrib import messages
#from django.http import HttpResponse
import datetime
#from django.views.generic import ListView

# Create your views here.


#listado de perfiles de menores
@login_required
def listar_perfiles_menores_view(request):
    menores = PerfilMenor.objects.filter(usuario_principal_id=request.user.id)
    return render(request, 'listar/perfilesMenores.html', {"menores": menores})


# Listado histórico de mediciones de un menor
@login_required
def historico_mediciones_menor_view(request, id):
    mediciones = MedicionCrecimiento.objects.filter(perfil_id=id)
    menor = PerfilMenor.objects.get(id=id)

    context = {
            'mediciones': mediciones,
            'menor': menor
        }

    return render(request, 'listar/historicoMedicionesMenor.html', context)


@login_required
def ficha_menor_view(request, id):
    #print(id)
    menor = PerfilMenor.objects.get(id=id)
    return render(request, 'fichaMenor.html', {'menor': menor})



# Formulario de creación de un perfil de menor
@login_required
def crear_perfil_menor_view(request):
    if request.method =='POST':
        crear_perfil_menor_form = CrearPerfilMenorForm(request.POST)
        # Access the currently logged-in user
        #usuario_principal = request.user
       

        if crear_perfil_menor_form.is_valid(): 
            perfil_menor = crear_perfil_menor_form.save(commit=False)
            perfil_menor.usuario_principal_id = request.user.id
            perfil_menor.save()
            return redirect('listar_menores')
    else:
        crear_perfil_menor_form = CrearPerfilMenorForm()
        return render(request, 'crear/crearPerfilMenor.html', {
        'crear_perfil_menor_form': crear_perfil_menor_form
        })
    


@login_required
def registrar_medicion_view(request, id):
    print(id)
    menor = PerfilMenor.objects.get(id=id)
    fecha_nacimiento = menor.fecha_nacimiento
    print(fecha_nacimiento)
    if request.method =='POST':
        registrar_medicion_form = RegistrarMedicionForm(request.POST)
        if registrar_medicion_form.is_valid():
             # Receive the submitted date as an instance of `datetime.date`.
            date: datetime.date = registrar_medicion_form.cleaned_data["fecha_medicion"]
            #fecha_medicion = registrar_medicion_form.cleaned_data['fecha_medicion'] 

          
            medicion = registrar_medicion_form.save(commit=False)
            medicion.perfil_id = id # se setea el id del perfil del manor
            medicion.save()
            messages.success(request, 'Medición registrada exitósamente!') 
            return redirect('registrar_medicion', id=id)
        else:
            # Form invalid, re-render with errors
            menor = PerfilMenor.objects.get(id=id)
            context = {'registrar_medicion_form': registrar_medicion_form, 'menor': menor}
            return render(request, 'fichaMenor.html', context)
    else:
        registrar_medicion_form = RegistrarMedicionForm()
        menor = PerfilMenor.objects.get(id=id)
        # Context dictionary to pass data to the template
        context = {
            'registrar_medicion_form': registrar_medicion_form,
            'menor': menor
        }
        return render(request, 'fichaMenor.html', context)
    



# vista del reporte simple de menor
def reporte_simple_view_function(request, id):
    # se obtienen los datos del menor (incluido sexo para decidir que tablas estadístias serán consultadas)
    menor = PerfilMenor.objects.get(id=id)
    sexo = menor.sexo
    # se obtiene la medición del menor con la fecha de medicion mas reciente
    #medicion = MedicionCrecimiento.objects.filter(perfil_id=id).order_by('-id').first()
    mensaje_talla = ""
    msg_recomendaciones_talla = ""
    msg_peso = ""
    msg_recomendaciones_peso = ""
    display_peso = ""
    display_talla = ""
    medicion = MedicionCrecimiento.objects.filter(perfil_id=id).order_by('-fecha_medicion').first()
    
    if medicion is not None:
        edad_anos = str(medicion.edad_anos)
        edad_meses = str(medicion.edad_meses)
        print(edad_anos)
        print(edad_meses)

        anos_meses_medicion = edad_anos+':'+edad_meses
        print(anos_meses_medicion)
        peso_medicion = medicion.peso
        txt_peso = str(medicion.peso) +' kg'


        display_peso = str(medicion.peso)+' kg' if medicion.peso is not None else ""
        print(display_peso) 

        display_talla = str(medicion.talla)+' cm' if medicion.talla is not None else ""
        print(display_talla) 

        talla_medicion = medicion.talla
        print(peso_medicion)
        print(talla_medicion)

        if sexo == 'F': 
            
            # Niñas
            # Talla
            print(TallaEdadNinasNac5AnosZscores.objects.get(anos_meses=anos_meses_medicion))
            talla_result = TallaEdadNinasNac5AnosZscores.objects.get(anos_meses=anos_meses_medicion)
            print('se imprimirá talla media niñas')
            print(talla_result.mediana)
        
            if talla_medicion is not None:
        
                if talla_medicion < talla_result.mediana:
                    mensaje_talla = f"La talla se encuentra por debajo de la mediana para niñas de {edad_anos} años y {edad_meses} meses ."
                    msg_recomendaciones_talla = f"Esta es una recomendación para cuando la talla está por debajo de la mediana para niñas de {edad_anos} años y {edad_meses} meses."
                
                elif talla_medicion > talla_result.mediana:
                    mensaje_talla = f"Talla por encima de la mediana para niñas de {edad_anos} años y {edad_meses} meses."  
                    msg_recomendaciones_talla = f"Esta es una recomendación para cuando la talla está por encima de la mediana para niñas de {edad_anos} años y {edad_meses} meses."

                else:          
                    mensaje_talla = f"Talla es igual a la mediana para niñas de {edad_anos} años y {edad_meses} meses."  
                    msg_recomendaciones_talla = f"Esta es una recomendación para cuando la talla es igual de la mediana para niñas de {edad_anos} años y {edad_meses} meses." 

            # Peso
            print(PesoEdadNinasNac5AnosZscores.objects.get(anos_meses=anos_meses_medicion))
            peso_result = PesoEdadNinasNac5AnosZscores.objects.get(anos_meses=anos_meses_medicion)
            print('se imprimirá mediana peso niñas')
            print(peso_result.mediana)

            if peso_medicion is not None:
        
                if peso_medicion < peso_result.mediana:
                    msg_peso = f"Peso por debajo de la mediana para niñas de {edad_anos} años y {edad_meses} meses."
                    msg_recomendaciones_peso = f"Esta es una recomendación para cuando el peso está por debajo de la mediana para niñas de {edad_anos} años y {edad_meses} meses."
                
                elif peso_medicion > peso_result.mediana:
                    msg_peso = f"Peso por encima de la mediana para niñas de {edad_anos} años y {edad_meses} meses."  
                    msg_recomendaciones_peso = f"Esta es una recomendación para cuando el peso está por encima de la mediana para niñas de {edad_anos} años y {edad_meses} meses."

                else:          
                    msg_peso = f"Peso es igual a la mediana para niñas de {edad_anos} años y {edad_meses} meses."  
                    msg_recomendaciones_peso = f"Esta es una recomendación para cuando el peso es igual de la mediana para niñas de {edad_anos} años y {edad_meses} meses." 




    
        else:
            # Niños
            # Talla
            print(TallaEdadNinosNac5AnosZscores.objects.get(anos_meses=anos_meses_medicion))
            talla_result = TallaEdadNinosNac5AnosZscores.objects.get(anos_meses=anos_meses_medicion)
            print('se imprimirá talla media niños')
            print(talla_result.mediana)

            mensaje_talla = ""
            msg_recomendaciones_talla = ""

            if talla_medicion is not None:    
            
                if  talla_medicion < talla_result.mediana:
                    mensaje_talla = f"La talla se encuentra por debajo de la mediana para niños de {edad_anos} años y {edad_meses} meses."
                    #msg_recomendaciones_talla = f"Esta es una recomendación para cuando la talla está por debajo de la mediana para niños de {edad_anos} años y {edad_meses} meses."
                    msg_recomendaciones_talla = f"Se recomienda mantener los controles periódicos y observar la evolución del crecimiento en el tiempo."
                
                elif talla_medicion > talla_result.mediana:
                    mensaje_talla = f"Talla por encima de la mediana para niños de {edad_anos} años y {edad_meses} meses."  
                    msg_recomendaciones_talla = f"Esta es una recomendación para cuando la talla está por encima de la mediana para niños de {edad_anos} años y {edad_meses} meses."

                else:          
                    mensaje_talla = f"Talla es igual a la mediana para niños de {edad_anos} años y {edad_meses} meses."  
                    msg_recomendaciones_talla = f"Esta es una recomendación para cuando la talla es igual de la mediana para niñas de {edad_anos} años y {edad_meses} meses." 

            # Peso
            print(PesoEdadNinosNac5AnosZscores.objects.get(anos_meses=anos_meses_medicion))
            peso_result = PesoEdadNinosNac5AnosZscores.objects.get(anos_meses=anos_meses_medicion)
            print('se imprimirá mediana peso niños')
            print(peso_result.mediana)

            if peso_medicion is not None:
        
                if peso_medicion < peso_result.mediana:
                    msg_peso = f"Peso por debajo de la mediana para niños de {edad_anos} años y {edad_meses} meses."
                    msg_recomendaciones_peso = f"Esta es una recomendación para cuando el peso está por debajo de la mediana para niños de {edad_anos} años y {edad_meses} meses."
                
                elif peso_medicion > peso_result.mediana:
                    msg_peso = f"Peso por encima de la mediana para niños de {edad_anos} años y {edad_meses} meses."  
                    msg_recomendaciones_peso = f"Esta es una recomendación para cuando el peso está por encima de la mediana para niños de {edad_anos} años y {edad_meses} meses."

                else:          
                    msg_peso = f"Peso es igual a la mediana para niños de {edad_anos} años y {edad_meses} meses."  
                    msg_recomendaciones_peso = f"Esta es una recomendación para cuando el peso es igual de la mediana para niños de {edad_anos} años y {edad_meses} meses." 

    
    
    
    
    
    
    
    
    
    
    
    
    context = {'medicion': medicion, 'menor': menor, 'mensaje_talla': mensaje_talla, 
               'msg_recomendaciones_talla': msg_recomendaciones_talla, 'display_peso': display_peso, 'display_talla': display_talla, 
               'msg_peso': msg_peso, 'msg_recomendaciones_peso': msg_recomendaciones_peso
               }
    return render(request, 'reporteSimpleMenor.html', context)