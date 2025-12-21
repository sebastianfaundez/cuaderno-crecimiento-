from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuarioForm, RegistroUsuarioSecundarioForm, PerfilForm
from .models import UsuarioSecundario, User

#home

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

# vista formulario de registro de usuario secundario
def registroUsuarioSecundario(request):
    if request.method =='POST':
        user_form=RegistroUsuarioSecundarioForm(request.POST)
        
        if user_form.is_valid(): 
            user=user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            usuario_secundario_id = user.id # se obtiene el ID del usuario secundario recien creado

            # aquí se debe insertar en la nueva tabla cuenta_usuario_secundario
            usuario_secundario = UsuarioSecundario()
            usuario_secundario.usuario_secundario_id = usuario_secundario_id
            usuario_secundario.usuario_principal_id = request.user.id
            usuario_secundario.save()
            # se redirige al listado de usuarios secundarios
            return redirect('usuarios_secundarios')
    else:
        user_form=RegistroUsuarioSecundarioForm()
        
    
    return render(request, 'registro/registroUsuarioSecundario.html', {
        'user_form': user_form
        
    })

#listado de usuarios secundarios de un usuario principal
@login_required
def usuarios_secundarios_view(request):
    print('linea 84 cuenta/views.py')
    print(request.user.id)
    #rel_usuarios_secundarios = UsuarioSecundario.objects.filter(usuario_principal_id=request.user.id)
    #data = UsuarioSecundario.objects.select_related('usuario_principal').filter(usuario_principal=request.user.id)
    #data = UsuarioSecundario.objects.select_related('usuario_principal').filter(usuario_principal_id=request.user.id)
    #data = User.objects.select_related('usuario_principal').filter(id=request.user.id)
    #data = User.objects.all()
    #users_with_specific_post = User.objects.filter(post__title='My First Post')
    #usuario = User()
    #secundarios = UsuarioSecundario.objects.select_related('usuario_principal').all()
    #print(UsuarioSecundario.objects.select_related('usuario_secundario').all().query)
    secundarios = User.objects.select_related('usuario_secundario').all()

    #print(data.__dict__)
    for secundario in secundarios:
        #temp = secundario.usuario_principal
        print(secundario.usuario_secundario.username)
        #print(secundario.__dict__)
        #print(d.user.id, d.user.name) # Accessing 'store' implicitly performs a join

    
   
    context = {
        'usuarios': secundarios,
    }
    return render(request, 'usuarios_secundarios.html', context)
