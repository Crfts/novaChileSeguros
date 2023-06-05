from django import forms
from .models import *

anos =(
    ("2023", "2023"),
    ("2022", "2022"),
    ("2021", "2021"),
    ("2020", "2020"),
    ("2019", "2019"),
)

precio =(
    ("1", "Menor precio"),
    ("2", "Mayor precio"),
)
class DateInput(forms.DateInput):
    input_type = 'date'



class Filtro(forms.Form):
    orden = forms.ChoiceField(choices= anos, required=False)
    companias = forms.ModelChoiceField(queryset= Compania.objects.all())
    Promocion = forms.ModelChoiceField  


class AutoCotizado(forms.Form):
    modelo = forms.ModelChoiceField(queryset= Modelo.objects.all())
    ano = forms.ChoiceField(choices=anos)
    patente = forms.CharField(max_length=8)
    marca = forms.ModelChoiceField(queryset= Marca.objects.all() )


class crearCotizacion(forms.Form):
    rut = forms.CharField(max_length= 10)
    telefono = forms.IntegerField(min_value=9000000, max_value=999999999)
    correo = forms.EmailField()
    fecha_nacimiento = forms.DateField(widget=DateInput)
    marca = forms.ModelChoiceField(queryset= Marca.objects.all() )
    patente = forms.CharField(max_length=8)
    modelo = forms.ModelChoiceField(queryset= Modelo.objects.all())
    ano = forms.ChoiceField(choices=anos)


class CotizanteForm(forms.ModelForm):
    class Meta:
        model = Cotizante
        fields = '__all__'
# class Cotizante(forms.Form):
#     nombre = forms.CharField(max_length= 30)
#     ap_pat = forms.CharField(max_length= 30)
#     ap_mat = forms.CharField(max_length=30)
#     rut = forms.CharField(max_length= 10)
#     telefono = forms.IntegerField(min_value=9000000, max_value=999999999)
#     correo = forms.EmailField()
#     fecha_nacimiento = forms.DateField(widget=DateInput)
#     marca = forms.ModelChoiceField(queryset= Marca.objects.all() )
#     patente = forms.CharField(max_length=8)
#     modelo = forms.ModelChoiceField(queryset= Modelo.objects.all())
#     ano = forms.ChoiceField(choices=anos)
