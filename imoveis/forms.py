from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from .models import Imovei
from django import forms
from .a import iddd, LISTA_Venda, LISTA_sn, LISTA_plus, LISTA_comodos, Semana, LISTA_autorização
from .a import  LISTA_ESTADOS, LISTA_CATEGORIAS, LISTA_telhado, LISTA_piso, LISTA_DADOS


class FiltrodeProcura(forms.Form):
    email = forms.EmailField(label=False)

class FormHomepage(forms.Form):
    email = forms.EmailField(label=False)

LISTA_FAVORITAR = (
    ('Favoritar', 'Favoritar'),
)

Lista_confirm = (
    ('Favoritar', 'Favoritar'),
)

class Compararr(forms.Form):
    confirm = forms.MultipleChoiceField(choices = Lista_confirm)

class CriarContaForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')



class Imoveis_filtro(forms.Form):
    tipo = forms.ChoiceField(required=False , choices=LISTA_DADOS)
    categoria = forms.ChoiceField(required=False ,choices=LISTA_CATEGORIAS)
    estado = forms.ChoiceField(required=False, choices=LISTA_ESTADOS) 
    cidade = forms.CharField(required=False, max_length=1000)
    bairro = forms.CharField(required=False,max_length=1000)
    valor = forms.IntegerField(required=False,)
    iptu = forms.IntegerField(required=False,)
    tipo_autorizacao = forms.ChoiceField(required=False, choices=LISTA_autorização)
    escritura = forms.ChoiceField(required=False, choices=LISTA_sn)
    mobiliado = forms.ChoiceField(required=False, choices=LISTA_sn)
    aceita_permuta = forms.ChoiceField(required=False, choices=LISTA_sn)
    imovel_desocupado = forms.ChoiceField(required=False, choices=LISTA_sn)
    imovel_quitado = forms.ChoiceField(required=False, choices=LISTA_sn)
    area_gourmet = forms.ChoiceField(required=False, choices=LISTA_sn)
    quintal_ou_jardim_ou_area_externa = forms.ChoiceField(required=False, choices=LISTA_sn)
    venda = forms.ChoiceField(required=False, choices=LISTA_Venda)
    qtde_andares = forms.IntegerField(required=False,)
    qtde_comodos = forms.IntegerField(required=False,)
    tamanho_piscinas = forms.IntegerField(required=False,)
    qtde_piscinas = forms.IntegerField(required=False,)
    tamanho_cozinha = forms.IntegerField(required=False,)
    qtde_cozinhas = forms.IntegerField(required=False,)
    tamanho_salas = forms.IntegerField(required=False,)
    qtde_salas = forms.IntegerField(required=False,)
    tamanho_dormitorios = forms.IntegerField(required=False,)
    qtde_dormitorios = forms.IntegerField(required=False,)
    tamanho_banheiros = forms.IntegerField(required=False,)
    qtde_banheiros = forms.IntegerField(required=False,)
    sendo_suites = forms.IntegerField(required=False,)
    idd = forms.CharField(required=False,max_length=1000)
    qtde_garagens = forms.IntegerField(required=False,)
    qtde_vagas = forms.IntegerField(required=False,)
    tamanho_quintal_ou_jardim_ou_area_externa = forms.IntegerField(required=False,)
    area_util = forms.IntegerField(required=False,)
    area_total = forms.IntegerField(required=False,)
    area_construida = forms.IntegerField(required=False,)
    material_telhado = forms.ChoiceField(required=False, choices=LISTA_telhado)
    material_piso = forms.ChoiceField(required=False, choices=LISTA_piso)
