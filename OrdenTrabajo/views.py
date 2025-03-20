from django.shortcuts import render
#from django.http import HttpResponse



# Create your views here.

def saludo(request):
    contexto = {'mensaje': 'Hola Django - Coder'} 
    return render(request, 'miapp\saludo.html', contexto)

def index(request):
    context = {"mensaje": "Bienvenidos a mi aplicación Django! **A éste texto lo llama desde Views**"}
    return render(request, "OrdenTrabajo\index.html", context)
