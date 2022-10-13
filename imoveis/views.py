from calendar import WEDNESDAY
from django.http import HttpResponseBadRequest, JsonResponse
from django.core import serializers
from re import A, I
import json
from django.http import HttpResponseForbidden, HttpResponseRedirect
from .enviaremail import send_email
from datetime import datetime
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Imagen, Imovei, Usuario, Corretores, Plantao, Todo
from django.views.generic.edit import FormMixin
from .forms import CriarContaForm, FormHomepage, Imoveis_filtro
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.db.models import Q
from .a import lista
import ast

# Create your views here.
class Homepage(FormView):
    template_name = "homepage.html"
    form_class = FormHomepage

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated: #usuario esta autenticado:
            # redireciona para a homeimoveis
            return redirect('imoveis:homeimoveis')
        else:
            return super().get(request, *args, **kwargs) # redireciona para a homepage

    def get_success_url(self):
        email = self.request.POST.get("email")
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('imoveis:login')
        else:
            return reverse('imoveis:criarconta')


class Homeimoveis(LoginRequiredMixin, ListView):
    template_name = "homeimoveis.html"
    model = Imovei





def Procurar(request):
    model = Imovei
    hoje = datetime.today().strftime('%A')
    if hoje == "Sunday":
        hoje = "Domingo"

    if hoje == "Monday":
        hoje = "Segunda-feira"

    if hoje == "Tuesday":
        hoje = "Terça-feira"

    if hoje == "Wednesday":
        hoje = "Quarta-feira"

    if hoje == "Thursday":
        hoje = "Quinta-feira"

    if hoje == "Friday":
        hoje = "Sexta-feira"

    if hoje == "Saturday":
        hoje = "Sábado"


    if request.method == "GET":
        imoveis_filtrados = Imovei.objects.all().order_by('-data_criacao')
        form = Imoveis_filtro()
        batata = 0
        for i in lista:
            batata+= 1
            print(form[i])
            separar = f"{i} {form[i]}"
        aff = 0
        for ae in form:
            for i in ae:
                aff += 1
                print(aff, i)
        corretores = "5514996892957"
        try:
            corretores = Corretores.objects.filter(dia=f'{hoje}')[0]
            corretores = corretores.numero_corretor

        except:
            corretores = "5514996892957"
        repete = 0
        filtro = [" ", " "]
        context = {
            'separar' : separar,
            'lista' : lista,
            'form' : form,
            'filtro' : filtro,
            'repete' : repete,
            'corretores' : corretores,
            'imoveis_filtrados' : imoveis_filtrados
        }
        return render(request, "procurar.html", context=context)
    elif request.method == "POST":
        
        imoveis_filtrados = Imovei.objects.all().order_by('-data_criacao')
        form = Imoveis_filtro(request.POST)
        filtro = [" ", " "]
        repete = 0
        corretores = "5514996892957"
        try:
            corretores = Corretores.objects.filter(dia=f'{hoje}')[0]
            corretores = corretores.numero_corretor

        except:
            corretores = "5514996892957"
            context = {
            'separar' : separar,
            'form' : form,
            'filtro' : filtro,
            'repete' : repete,
            'corretores' : corretores,
            'imoveis_filtrados' : imoveis_filtrados
        }

        q = Q()

        for i in lista:
            
            if form.data[i] != 'Vazio':
                print(form.data)
                q &= eval("Q({}=form.data['{}'])".format(i, i))
                imoveis_filtrados = Imovei.objects.filter(q).all
                filtro.append(form.data[i])
                    
                            
                repete = repete + 1
                context = {
                'separar' : separar,
                'lista' : lista,
                'form' : form,
                'filtro' : filtro,
                'repete' : repete,
                'corretores' : corretores,
                'imoveis_filtrados' : imoveis_filtrados
                }
            return render(request, "procurar.html", context=context)


#########################################################################################################################################################################
#########################################################################################################################################################################
#########################################################################################################################################################################







def home(request):
    return render(request, "home.html")


def aja_x(request):
    # request.is_ajax() is deprecated since django 3.1
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    usuario = request.user
    if is_ajax:
        if request.method == 'GET':
            form = Imoveis_filtro()
            for imovei in Imovei.objects.all():
                contagem = 0
                segcontagem = 0
                if usuario.permitidos_img == imovei:
                    print("A")
            return render(request, "procurar.html", context=context)
        if request.method == 'POST':
            data = json.load(request)
            todo = data.get('payload')
            print(todo.get('task'))
            Todo.objects.create(task=todo['task'], completed=todo['completed'])
            return JsonResponse({'status': 'Todo added!'})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        if request.method == 'GET':
            imoveis = list(Imovei.objects.filter(idd=1).values())
            print(imoveis)
            return JsonResponse({'context': imoveis})



#########################################################################################################################################################################
#########################################################################################################################################################################
#########################################################################################################################################################################




class Corretor(LoginRequiredMixin, ListView):
    template_name = "corretor.html"
    model = Imovei

class Favoritos(LoginRequiredMixin, ListView):
    template_name = "favoritos.html"
    model = Imovei


class Anunciarimovel(LoginRequiredMixin, ListView):
    template_name = "anunciarimovel.html"
    model = Imovei




class Contato_Corretores(LoginRequiredMixin, DetailView):
    template_name = "contato_corretores.html"
    model = Imovei

    # object -> 1 item do nosso modelo

    def get(self, request, *args, **kwargs):
        # contabilizar uma visualização
        imovei = self.get_object()
        usuario = request.user
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Contato_Corretores, self).get_context_data(**kwargs)
        hoje = datetime.today().strftime('%A')
        if hoje == "Sunday":
            hoje = "Domingo"

        if hoje == "Monday":
            hoje = "Segunda-feira"

        if hoje == "Tuesday":
            hoje = "Terça-feira"

        if hoje == "Wednesday":
            hoje = "Quarta-feira"

        if hoje == "Thursday":
            hoje = "Quinta-feira"

        if hoje == "Friday":
            hoje = "Sexta-feira"

        if hoje == "Saturday":
            hoje = "Sábado"
        corretor = ['', '']
        try:
            corretores = Plantao.objects.filter(dias=f'{hoje}')[0]
            corretoress = Corretores.objects.all
            corretor = ['', '']
            for correto in corretoress:
                if correto == corretores:
                    corretor.append(correto)

            context["corretor"] = corretor
           

        except:
            correto = Corretores.objects.filter(corretor='Imobiliária')[0]
            corretor.append(correto)
            context["corretor"] = corretor

        corretores = Corretores.objects.all
        context["corretores"] = corretores
        plantao = Plantao.objects.all
        context["plantao"] = plantao
        return context







    

class Detalhesimovel(LoginRequiredMixin, DetailView):



    # object -> 1 item do nosso modelo

    def get(self, request, *args, **kwargs):
        # contabilizar uma visualização
        imovei = self.get_object()
        usuario = request.user
        favoritos = request.user.favoritos
        ata = imovei.idd
        usuario.ultimo_visto = ata
        usuario.save()
        contagem = 0
        segcontagem = 0
        for imovel in usuario.imoveis_vistos.all():
            contagem += 1
        for imovel in usuario.imoveis_vistos.all():
            segcontagem += 1 
            if imovel == imovei:
                break
            if segcontagem == contagem:
                imovei.visualizacoes += 1
                imovei.save()
        usuario.imoveis_vistos.remove(imovei)
        usuario.imoveis_vistos.add(imovei)
        return super().get(request, *args, **kwargs) # redireciona o usuario para a url final
    template_name = "detalhesimovel.html"
    model = Imovei
    def get_context_data(self , **kwargs):
        context = super(Detalhesimovel, self).get_context_data(**kwargs)
        # filtrar a minha tabela de imoveis pegando os imoveis cuja categoria é igual a categoria do imovel da página (object)
        # self.get_object()
        imovei = self.get_object()

        usuario = self.request.user
        favoritos = usuario.favoritos.all()
        liberado = "nao"
        for i in usuario.favoritos.all():
            if i == imovei:
                liberado = "sim"
        context["liberado"] = liberado

        imovei = self.get_object()
        imoveis_relacionados = Imovei.objects.filter(categoria=self.get_object().categoria)[0:5]
        imagen = Imagen.objects.filter(question=imovei.idd)

        
    
        context["imoveis_relacionados"] = imoveis_relacionados
        context["imagen"] = imagen
        context["favoritos"] = favoritos
        return context




class Compararimovel(LoginRequiredMixin, DetailView):



    # object -> 1 item do nosso modelo

    def get(self, request, *args, **kwargs):
        # contabilizar uma visualização
        imovei = self.get_object()
        usuario = request.user
        favoritos = request.user.favoritos
        ata = imovei.idd
        usuario.ultimo_visto = ata
        usuario.save()
        contagem = 0
        segcontagem = 0
        for imovel in usuario.imoveis_vistos.all():
            contagem += 1
        for imovel in usuario.imoveis_vistos.all():
            segcontagem += 1 
            if imovel == imovei:
                break
            if segcontagem == contagem:
                imovei.visualizacoes += 1
                imovei.save()
        usuario.imoveis_vistos.add(imovei)
        return super().get(request, *args, **kwargs) # redireciona o usuario para a url final
    template_name = "compararimovel.html"
    model = Imovei
    def get_context_data(self , **kwargs):
        context = super(Compararimovel, self).get_context_data(**kwargs)
        # filtrar a minha tabela de imoveis pegando os imoveis cuja categoria é igual a categoria do imovel da página (object)
        # self.get_object()
        imovei = self.get_object()

        usuario = self.request.user
        favoritos = usuario.favoritos.all()
        liberado = "nao"
        for i in usuario.favoritos.all():
            if i == imovei:
                liberado = "sim"
        context["liberado"] = liberado

        imovei = self.get_object()
        imoveis_relacionados = Imovei.objects.filter(categoria=self.get_object().categoria)[0:5]
        imagen = Imagen.objects.filter(question=imovei.idd)
    
        context["imoveis_relacionados"] = imoveis_relacionados
        context["imagen"] = imagen
        context["favoritos"] = favoritos
        return context

class Comparar_tabela(LoginRequiredMixin, DetailView):



    # object -> 1 item do nosso modelo

    def get(self, request, *args, **kwargs):
        # contabilizar uma visualização
        imovei = self.get_object()
        usuario = request.user
        favoritos = request.user.favoritos
        ata = imovei.idd
        usuario.ultimo_visto = ata
        usuario.save()
        contagem = 0
        segcontagem = 0
        for imovel in usuario.imoveis_vistos.all():
            contagem += 1
        for imovel in usuario.imoveis_vistos.all():
            segcontagem += 1 
            if imovel == imovei:
                break
            if segcontagem == contagem:
                imovei.visualizacoes += 1
                imovei.save()
        usuario.imoveis_vistos.add(imovei)
        return super().get(request, *args, **kwargs) # redireciona o usuario para a url final
    template_name = "Comparar_tabela.html"
    model = Imovei
    def get_context_data(self , **kwargs):
        context = super(Comparar_tabela, self).get_context_data(**kwargs)
        # filtrar a minha tabela de imoveis pegando os imoveis cuja categoria é igual a categoria do imovel da página (object)
        # self.get_object()
        imovei = self.get_object()

        usuario = self.request.user
        favoritos = usuario.favoritos.all()
        liberado = "nao"
        for i in usuario.favoritos.all():
            if i == imovei:
                liberado = "sim"
        context["liberado"] = liberado

        imovei = self.get_object()
        imoveis_relacionados = Imovei.objects.filter(categoria=self.get_object().categoria)[0:5]
        imagen = Imagen.objects.filter(question=imovei.idd)
    
        context["imoveis_relacionados"] = imoveis_relacionados
        context["imagen"] = imagen
        context["favoritos"] = favoritos
        return context


        
class Pesquisa_id(LoginRequiredMixin, ListView):
    template_name = "pesquisa_id.html"
    model = Imovei

    #object_list
    def get_queryset(self):
        termo_pesquisa_id = self.request.GET.get('query')
        if termo_pesquisa_id:
            object_list = self.model.objects.filter(idd__icontains=termo_pesquisa_id)
            return object_list
        else:
            return None


class Paginaperfil(LoginRequiredMixin, UpdateView):
    template_name = "editarperfil.html"
    model = Usuario
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('imoveis:homeimoveis')


class Criarconta(FormView):
    template_name = "criarconta.html"
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('imoveis:login')

# def homepage(request):
#     return render(request, "homepage.html")

# url - view - html
# def homeimoveis(request):
#     context = {}
#     lista_filmes = Filme.objects.all()
#     context['lista_filmes'] = lista_filmes
#     return render(request, "homeimoveis.html", context)



class Favoritar(LoginRequiredMixin, DetailView):
    template_name = "detalhesimovel.html"
    model = Imovei


    # object -> 1 item do nosso modelo
    def get(self, request, *args, **kwargs):
        # contabilizar uma visualização
        imovei = self.get_object()
        usuario = request.user

        contagem = 0
        segcontagem = 0
        for imovel in usuario.favoritos.all():
            contagem += 1
        for imovel in usuario.favoritos.all():
            segcontagem += 1 
            if imovel == imovei:
                usuario.favoritos.remove(imovei)
                break
            if segcontagem == contagem:
                usuario.favoritos.add(imovei)
                imovei.save()
        return redirect('imoveis:detalhesimovel', imovei.pk)