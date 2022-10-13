import email
from django.db.models import F
from django.db import models
from django.utils import timezone
from datetime import timedelta
import uuid
from django.contrib.auth.models import AbstractUser
from .a import iddd, LISTA_Venda, LISTA_sn, LISTA_plus, LISTA_comodos, Semana, LISTA_autorização
from .a import  LISTA_ESTADOS, LISTA_CATEGORIAS, LISTA_telhado, LISTA_piso, LISTA_DADOS
# Create your models here.

#################################################################
class Todo(models.Model):
    task = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task
#################################################################


class Imovei(models.Model):




# infos proprietario
    proprietario = models.CharField(max_length=1000, default="")
    telefone_proprietario = models.CharField(max_length=1000, default="")
    email_proprietario = models.CharField(max_length=1000, default="")
    nota_proprietario = models.TextField(max_length=1000, default="")




# localização
    estado = models.CharField(max_length=20, choices=LISTA_ESTADOS, default="SP") 
    cidade = models.CharField(max_length=1000, default="")
    bairro = models.CharField(max_length=1000, default="")
    rua = models.CharField(max_length=1000, default="")
    numero = models.IntegerField(default=0)
    cep = models.CharField(max_length=1000, default="")


# visual
    thumb = models.ImageField(upload_to='img_imoveis')
    titulo = models.CharField(max_length=1000, default="")
    descricao = models.TextField(max_length=1000, default="Vazio")

# detalhes tipo
    tipo = models.CharField(max_length=50, choices=LISTA_DADOS, default="Vazio")
    categoria = models.CharField(max_length=20, choices=LISTA_CATEGORIAS, default="Vazio")
    venda = models.CharField(max_length=20, choices=LISTA_Venda, default="Vazio")
    tipo_autorizacao = models.CharField(max_length=20, choices=LISTA_autorização, default="Vazio")



# valores mutáveis
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)
    idd = models.CharField(default=iddd, max_length=1000)


# valores
    valor = models.IntegerField(default=0)
    iptu = models.IntegerField(default=0)
    taxa_condominio = models.IntegerField(default=0)
    

# S/N
    consulta_prec = models.CharField(max_length=20, choices=LISTA_sn, default="Vazio")
    consulta_loc = models.CharField(max_length=20, choices=LISTA_sn, default="Vazio")
    consulta_img = models.CharField(max_length=20, choices=LISTA_sn, default="Vazio")
    escritura = models.CharField(max_length=20, choices=LISTA_sn, default="Vazio")
    mobiliado = models.CharField(max_length=20, choices=LISTA_sn, default="Vazio")
    aceita_permuta = models.CharField(max_length=20, choices=LISTA_sn, default="Vazio")
    imovel_desocupado = models.CharField(max_length=20, choices=LISTA_sn, default="Vazio")
    imovel_quitado = models.CharField(max_length=20, choices=LISTA_sn, default="Vazio")




# links
    vídeo_link = models.CharField(max_length=1000, default="#")
    mais_link = models.CharField(max_length=1000, default="#")
    link_slides = models.CharField(max_length=1000, default="#")
    link_maps= models.CharField(max_length=1000, default="#")


# medidas de área
    area_util = models.IntegerField(default=0)
    area_total = models.IntegerField(default=0)
    area_construida = models.IntegerField(default=0)



#materiais
    material_telhado = models.CharField(max_length=20, choices=LISTA_telhado, default="Vazio")
    material_piso = models.CharField(max_length=20, choices=LISTA_piso, default="Vazio")



# infos do corretor
    interessados =  models.TextField(max_length=10000, default="Vazio")
    responsavel_captacao = models.CharField(max_length=1000, default="")
    marketing = models.TextField(max_length=100, default="")
    observacoes_corretores = models.CharField(max_length=1000, default="")


# quantitativos
    qtde_andares = models.IntegerField(default=0)
    qtde_comodos = models.IntegerField(default=0)

    def __str__(self):
        return self.idd

class Imagen(models.Model): 
    imagem = models.ImageField(upload_to='img_imoveis') 
    link_comodo = models.CharField(max_length=10000, default="#") 
    comodo = models.CharField(max_length=30, choices=LISTA_comodos, default="Vazio") 
    tamanho_comodo = models.IntegerField(default=0) 

    
    plus_comodo = models.CharField(max_length=30, choices=LISTA_plus, default="Vazio") 
    plus_valor = models.IntegerField(default=0)

    ligacao_comodo = models.CharField(max_length=1000, default="")
    
    question = models.ForeignKey(Imovei, on_delete=models.CASCADE) 
    def __str__(self): 
        return self.question and self.comodo


# criar o imovel


class Corretores(models.Model):
    imagem = models.ImageField(upload_to='img_imoveis')
    corretor = models.CharField(max_length=1000, default="")
    numero_corretor = models.CharField(max_length=1000, default="")
    email_corretor = models.CharField(max_length=1000, default="")
    instagram_corretor = models.CharField(max_length=1000, default="")
    facebook_corretor = models.CharField(max_length=1000, default="")
    def __str__(self):
        return self.corretor

class Plantao(models.Model):
    dias = models.CharField(max_length=1000,choices=Semana, default="")
    horas = models.CharField(max_length=1000, default="")
    question = models.ForeignKey(Corretores, on_delete=models.CASCADE)
    def __str__(self):
        return self.dias


class Usuario(AbstractUser):
    imoveis_vistos = models.ManyToManyField("Imovei", related_name='vistos')
    favoritos = models.ManyToManyField("Imovei", related_name='fa')
    permitidos_img = models.ManyToManyField("Imovei", related_name='per_img')
    permitidos_loc = models.ManyToManyField("Imovei", related_name='per_loc')
    permitidos_prec = models.ManyToManyField("Imovei", related_name='per_prec')
    admin = models.CharField(max_length=20, choices=LISTA_sn, default="Vazio")
    ultimo_visto = models.CharField(max_length=1000, default="")
    comparar = models.CharField(max_length=1000, default="")