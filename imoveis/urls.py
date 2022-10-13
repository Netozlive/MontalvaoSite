# url - view - template
from django.views.generic import TemplateView
from django.urls import path, reverse_lazy
from .views import Homeimoveis, Homepage, Detalhesimovel,Favoritar, Pesquisa_id, Paginaperfil, Criarconta, Procurar, Contato_Corretores , Favoritos, Corretor, Anunciarimovel, Compararimovel, Comparar_tabela, home, aja_x
from django.contrib.auth import views as auth_view

app_name = 'imoveis'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('imoveis/', Homeimoveis.as_view(), name='homeimoveis'),
    path('imovel/<int:pk>', Detalhesimovel.as_view(), name='detalhesimovel'),
    path('comparar/<int:pk>', Compararimovel.as_view(), name='compararimovel'),
    path('comparar/tabela/<int:pk>', Comparar_tabela.as_view(), name='comparar_tabela'),
    path('pesquisa_id/', Pesquisa_id.as_view(), name='pesquisa_id'),
    path('corretor/', Corretor.as_view(), name='corretor'),
    path('favoritos/', Favoritos.as_view(), name='favoritos'),
    path('favorito/<int:pk>', Favoritar.as_view(), name='favorito'),
    path('contato/corretores/<int:pk>', Contato_Corretores.as_view(), name='contato_corretores'),
    path('anunciarimovel/', Anunciarimovel.as_view(), name='anunciarimovel'),
    path('procurar/', Procurar, name='procurar'),
#########################################################################################################################################################################
    path('bah/', home, name='home'),
    path('bah/todos/', aja_x, name='todos'),

#########################################################################################################################################################################

    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editarperfil/<int:pk>', Paginaperfil.as_view(), name='editarperfil'),
    path('criarconta/', Criarconta.as_view(), name='criarconta'),
    path('mudarsenha/', auth_view.PasswordChangeView.as_view(template_name='editarperfil.html',
                                                             success_url=reverse_lazy('imoveis:homeimoveis')), name='mudarsenha'),
]