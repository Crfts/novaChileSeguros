from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.

def main(request):
    form = AutoCotizado()
    return render(request, 'cotizador/main.html', {'form' : form})

def mostrarPrecios(request):
    if request.method == 'POST':
        marca = Marca.objects.filter(marca = request.POST.get('marca')) 
        modelo = request.POST.get('modelo')
        ano = request.POST.get('ano')
        posts = ValorCotizacion.objects.all()
        context = {'marca': marca,'modelo': modelo, 'ano': ano, 'posts': posts }
        return render(request, 'cotizador/precios.html', context)
    else:
        # Si no es una solicitud POST, redirigir al usuario a la página del formulario
        return redirect('main')
    
def comprar(request):
    seguro_id = request.GET.get('seguro_id')
    posts = ValorCotizacion.objects.filter(id_cotizacion = seguro_id).first()
    form = CotizanteForm()
    return render(request, 'cotizador/comprar.html', {'form' : form ,'seguro_id' : seguro_id, 'posts': posts  })