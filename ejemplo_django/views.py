from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import estudiante

# Create your views here.

informacion_usuarios = [['Alexander','Segovia'],['Javier','Hilario'],['Martin','Leiva']]

def index(request):
    return HttpResponse('Mi primera aplicación web')

def hola(request):
    lista_elementos = ['Python','Django','Flask','Javascript','Docker']
    return render(request,'ejemplo_django/hola.html',{
        'lista_elementos':lista_elementos,
        'm2':'Este es un segundo mensaje (2)',
    })

def hastaLuego(request):
    return render(request,'ejemplo_django/hastaLuego.html')

def usuariosInfo(request):
    if request.method == 'POST':
        nombreUsuario = request.POST.get('nombreUsuario')
        apellidoUsuario = request.POST.get('usuarioApellido')
        codigoUsuario = request.POST.get('codigoUsuario')
        direccionUsuario = request.POST.get('direccionUsuario')
        emailUsuario = request.POST.get('emailUsuario')
        informacion_usuarios.append([nombreUsuario,apellidoUsuario])
        estudiante(nombre=nombreUsuario, apellido=direccionUsuario, codigo=codigoUsuario, direccion=direccionUsuario, email=emailUsuario).save()
        return render(request,'ejemplo_django/usuariosInfo.html',{
            'informacion_usuarios':estudiante.objects.all(),
        })
    return render(request,'ejemplo_django/usuariosInfo.html',{
        'informacion_usuarios':estudiante.objects.all(),
    })