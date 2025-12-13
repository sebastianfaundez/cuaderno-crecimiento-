from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuarioForm, PerfilForm

# Create your views here.
def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password') 


        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('panel_de_control')
        else: 
            messages.error(request, 'Usuario o clave incorrectos!')

    return render(request, 'login.html')

@login_required
def control_view(request):
    return render(request, 'panel_de_control.html')

def registro(request):
    if request.method =='POST':
        user_form=RegistroUsuarioForm(request.POST)
        perfil_form=PerfilForm(request.POST)

        if user_form.is_valid() and perfil_form.is_valid(): 
            user=user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            perfil=perfil_form.save(commit=False)
            perfil.user=user
            perfil.save()
            
            return redirect('login')
    else:
        user_form=RegistroUsuarioForm()
        perfil_form=PerfilForm()
    
    return render(request, 'registro/registro.html', {
        'user_form': user_form,
        'perfil_form': perfil_form
    })