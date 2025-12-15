from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CrearPerfilMenorForm
from .forms import RegistrarMedicionForm
from .models import PerfilMenor
from django.contrib import messages

# Create your views here.


#listado de perfiles de menores
@login_required
def listar_perfiles_menores_view(request):
    menores = PerfilMenor.objects.filter(usuario_principal_id=request.user.id)
    return render(request, 'listar/perfilesMenores.html', {"menores": menores})


@login_required
def ficha_menor_view(request, id):
    #print(id)
    menor = PerfilMenor.objects.get(id=id)
    return render(request, 'fichaMenor.html', {'menor': menor})




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
    if request.method =='POST':
        registrar_medicion_form = RegistrarMedicionForm(request.POST)
        if registrar_medicion_form.is_valid(): 
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