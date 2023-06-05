from django.contrib import admin
from django.apps import apps
from .models import *

# Register your models here.
admin.site.register(ValorCotizacion)
admin.site.register(Auto)
admin.site.register(AutoReemplazo)
admin.site.register(Compania)
admin.site.register(Deducible)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Producto)
admin.site.register(Promocion)
admin.site.register(TipoDano)
