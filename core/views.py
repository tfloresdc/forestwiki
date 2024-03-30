from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, "inicio.html")

def foro(request):
    return render(request, "forowiki.html")

def iniciarSesion(request):
    return render(request, "inicio_sesion_wiki.html")

def registrarse(request):
    return render(request, "registrase_wiki.html")

def miCuenta(request):
    return render(request, "micuentatf.html")

def recuperarConstrasena(request):
    return render(request, "recuperarcontra.html")