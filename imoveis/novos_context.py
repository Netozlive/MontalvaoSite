from re import A
from .models import Imovei
from django.db.models import F
from  pathlib  import  Path
caminho = Path(__file__).resolve().parent.parent
def lista_imoveis_recentes(request):
    lista_imoveis = Imovei.objects.all().order_by('-data_criacao')
    if lista_imoveis:
        imovel_destaque = lista_imoveis[0]
    else:
        imovel_destaque = None
    return {"lista_imoveis_recentes": lista_imoveis, "imovel_destaque": imovel_destaque}

#reporter = Eita.objects.get(pk=reporter.pk)

def verificacao(request):
    arquivo = open(f"{caminho}/static/cont/contagem.txt", "r")
    ixi = arquivo.read()
    ixi = int(ixi)
    for i in range(ixi):
        if i != 1:
            if i != 2:
                a = i-1
            if Imovei.idd == i:
                #imoveii = Imovei.objects.get(pk=a)
                #print(imovei)
                print('imoveii')
            #if imovei == imoveii:
             #   imovei.idd = int(Imovei.idd) + 1
              #  imovei.save()
    return()

def qtde(request):
    imovei = Imovei.objects.all()
    qtdd = 0
    for i in imovei:
        
        qtdd= int(i.pk)
    qtdd += 1
    arquivo = open(f"{caminho}/static/cont/contagem.txt", "w")
    arquivo.write(str(qtdd))

    reporter = Imovei.objects.filter(idd=qtdd).order_by('-data_criacao')
    if reporter == qtdd:
        reporter.idd = int(F('idd')) + 1
        reporter.save()
        reporter.refresh_from_db()

    return ()
def lista_imoveis_emalta(request):
    lista_imoveis = Imovei.objects.all().order_by('-visualizacoes')[0:8]
    return {"lista_imoveis_emalta": lista_imoveis}


def imoveis_apartamento(request):
    imoveis_apartamento = Imovei.objects.filter(categoria="Apartamento")[0:5]
    return {"imoveis_apartamento" : imoveis_apartamento}

def imoveis_casa(request):
    imoveis_casa = Imovei.objects.filter(categoria="Casa")[0:5]
    return {"imoveis_casa" : imoveis_casa}

def imoveis_terreno(request):
    imoveis_terreno = Imovei.objects.filter(categoria="Terreno")[0:5]
    return {"imoveis_terreno" : imoveis_terreno}
    
def imoveis_comercial(request):
    imoveis_comercial = Imovei.objects.filter(categoria="Imovel_comercial")[0:5]
    return {"imoveis_comercial" : imoveis_comercial}

def imoveis_rural(request):
    imoveis_rural = Imovei.objects.filter(categoria="Imovel_rural")[0:5]
    return {"Imovel_rural" : imoveis_rural}