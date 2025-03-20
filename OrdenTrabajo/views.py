from django.shortcuts import render, get_object_or_404
from models import Herramienta, Operario, OT

#from django.http import HttpResponse



# Create your views here.

#def saludo(request):
#    contexto = {'mensaje': 'Hola Django - Coder'} 
#    return render(request, 'miapp\saludo.html', contexto)

def index(request):
    context = {"mensaje": "Bienvenidos a mi aplicación Django! **A éste texto lo llama desde Views**"}
    return render(request, "OrdenTrabajo\index.html", context)

def lista_operarios(request):
    operarios = Operario.objects.all()
    return render(request, 'OrdenTrabajo/operarios_list.html', {'operarios': operarios})

def detalle_operario(request, pk):
    operario = get_object_or_404(Operario, pk=pk)
    return render(request, 'OrdenTrabajo/operarios_detail.html', {'operario': operario})



def lista_herramientas(request):
    herramientas = Herramienta.objects.all()
    return render(request, 'OrdenTrabajo/herramientas_list.html', {'herramientas': herramientas})

def detalle_herramienta(request, pk):
    herramienta = get_object_or_404(Herramienta, pk=pk)
    return render(request, 'OrdenTrabajo/herramientas_detail.html', {'herramienta': herramienta})



def lista_ots(request):
    ots = OT.objects.all()
    return render(request, 'OrdenTrabajo/OTs_list.html', {'ots': ots})

def detalle_ot(request, pk):
    ordtra = get_object_or_404(OT, pk=pk)
    return render(request, 'OrdenTrabajo/OTs_detail.html', {'ordtra': ordtra})