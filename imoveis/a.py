from MontalvaoSite.settings import STATICFILES_DIRS
from  pathlib  import  Path
caminho = Path(__file__).resolve().parent.parent


lista = [
    # infos proprietario
   # 'proprietario',
    #'telefone_proprietario',
    #'email_proprietario' ,
    #'nota_proprietario',




# localização
    'estado',
   # 'cidade',
    #'bairro',
    #'rua',
  #  'numero' ,
   # 'cep' ,


# visual
    #'thumb' ,
    #'titulo' ,
    #'descricao' ,

# detalhes tipo
    #'tipo' ,
    #'categoria' ,
    #'venda' ,
    #'tipo_autorizacao' ,



# valores mutáveis
   # 'visualizacoes',
    #'data_criacao',
    #'idd' ,


# valores
   # 'valor' ,
    #'iptu' ,
    #'taxa_condominio',
    

# S/N
 #   'consulta',
  #  'escritura',
   # 'mobiliado',
    #'aceita_permuta',
  # ' imovel_desocupado',
   # 'imovel_quitado',




# links
  #  'vídeo_link' ,
   # 'mais_link' ,
    #'link_slides' ,
    #'link_maps',


# medidas de área
    #'area_util' ,
    #'area_total',
    #'area_construida',



#materiais
   # 'material_telhado' ,
    #'material_piso' ,


# infos do corretor
  #  'interessados' ,
   # 'responsavel_captacao' ,
    #'marketing' ,
    #'observacoes_corretores',


# quantitativos
   # 'qtde_andares',
    #'qtde_comodos',
]







def iddd():
    arquivo = open(f"{caminho}/static/cont/contagem.txt", "r")
    ixi = arquivo.read()
    idd = int(ixi)
    idd = str(idd)

    return idd


def iddd1():
    arquivo = open("C:/Users/anaca/Desktop/Nova pasta/MontalvaoSite/MontalvaoSite/teste.txt", "r")
    ixi = arquivo.read()
    ide = int(ixi) + 2
    ide = str(ide)
    return ide








LISTA_Venda = (
    ("Vazio", "Vazio"),
    ('venda', 'venda'),
    ('vendido', 'vendido'),
    ('aluguel', 'aluguel'),
)

LISTA_sn = (
    ("Vazio", "Vazio"),
    ('sim', 'sim'),
    ('nao', 'nao'),
)
LISTA_plus = (
    ("Vazio", "Vazio"),
    ('Banheiro', 'Banheiro'),
    ('Cozinha', 'Cozinha'),
    ('Dorm', 'Dorm'),
    ('Banheiro', 'Banheiro'),
    ('Sendo Suítes', 'Sendo Suítes'),
    ('quintal/jardim/area_externa', 'quintal/jardim/area_externa'),
    ('Piscina', 'Piscina'),
    ('Garagem', 'Garagem'),
    ('Personalizado', 'Personalizado'),    
)

LISTA_comodos = (
("Vazio", "Vazio"),
("Área de serviço", "Área de serviço"), 
("Área_Gourmet", "Área_Gourmet"),
("Banheiro", "Banheiro"),
("Closet", "Closet") ,
("Corredor", "Corredor"),
("Cozinha", "Cozinha"),
("Deck", "Deck"),
("Despensa", "Despensa"),
("Dorm", "Dorm"),
("Edícula", "Edícula"),
("Escadas", "Escadas"),
("Escritório", "Escritório"),
("Faixada", "Faixada",),
("Garagem", "Garagem",),
("Jardim de inverno", "Jardim de inverno"),
("Lavabo", "Lavabo"),
("Piscina", "Piscina"),
("quintal/jardim/area_externa", "quintal/jardim/area_externa"),
("Sacada", "Sacada"),
("Sala de jantar", "Sala de jantar" ),
("Sala de tv", "Sala de tv"),
("Sala de visita", "Sala de visita"),
("Sendo Suítes", "Sendo Suítes"),
("Varanda", "Varanda"),  
("Personalizado", "Personalizado"),
)

Semana = (
    ("Domingo", "Domingo"),
    ('Segunda-feira', 'Segunda-feira'),
    ('Terça-feira', 'Terça-feira'),
    ('Quarta-feira', 'Quarta-feira'),
    ('Quinta-feira', 'Quinta-feira'),
    ('Sexta-feira', 'Sexta-feira'),
    ('Sábado', 'Sábado'),
)


LISTA_autorização = (
    ("Vazio", "Vazio"),
    ('exclusivo', 'exclusivo'),
    ('sem_exclusividade', 'sem_exclusividade'),
)

LISTA_ESTADOS = (
    ("Vazio", "Vazio"),
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins')
)

LISTA_CATEGORIAS = (
    ("Vazio", "Vazio"),
    ("Apartamento", "Apartamento"),
    ("Casa", "Casa"),
    ("Terreno", "Terreno"),
    ("Rancho", "Rancho"),
    ("Sitio", "Sitio"),
    ("Fazenda", "Fazenda"),
    ("Fabrica", "Fabrica"),

)

LISTA_telhado= (
    ("Vazio", "Vazio"),
    ("Laje", "Laje"),
    ("Forro", "Forro"),
)

LISTA_piso= (
    ("Vazio", "Vazio"),
    ("Laje", "Laje"),
    ("Forro", "Forro"),
)

LISTA_DADOS = (
    ("Vazio", "Vazio"),
    ("Residencial", "Residencial"),
    ("Comercial", "Comercial"),
    ("Industrial", "Industrial"),
    ("Rural", "Rural"),
    ("Condominio", "Condominio"),
    ("Comercial/Residencial", "Comercial/Residencial"),
)