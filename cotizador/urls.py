from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name =  "main"),
    path('precios/', mostrarPrecios, name="mostrarPrecios"),
    path('precios/comprar/', comprar, name="comprar"),
]
