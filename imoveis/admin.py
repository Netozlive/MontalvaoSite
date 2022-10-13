from django.contrib import admin

from .models import Usuario, Imovei, Imagen, Corretores, Plantao
from django.contrib.auth.admin import UserAdmin




class ChoiceInline(admin.TabularInline):
    model = Imagen
    class Media:
        css = {
                'all': ('css/ui.css',)
        }
    classes = ['bah',]




class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
      
        ('Informacoes do Proprietário', {'fields': ( 'proprietario', 
              'telefone_proprietario',
               'email_proprietario',
                'nota_proprietario'), 'classes': ['collapse']}),

      (' Captação ', {'fields': ('responsavel_captacao',
       'marketing'), 'classes': ['collapse']}),
        ('Localização', {'fields': ( 'estado',
               'cidade', 
               'bairro',
                'rua', 
                'numero',
                 'cep'), 'classes': ['collapse']}),
                 
        ('Informações', {'fields': ('tipo',
                       'categoria', 
               'descricao',
               'visualizacoes',
               'thumb',
                'titulo',
                'data_criacao'), 'classes': ['collapse']}),


        ('Quantidades', {'fields': ('qtde_andares', 
        'qtde_comodos' ), 'classes': ['collapse']}),
        ('Medidas', {'fields': ('area_total',
           'area_construida',
            'area_util'), 'classes': ['collapse']}),
        ('Características', {'fields': ( 'material_telhado',
         'material_piso',
          'escritura', 
          'tipo_autorizacao', 
          'mobiliado', 
          'aceita_permuta', 
          'imovel_desocupado', 
          'imovel_quitado', 
          'venda'), 'classes': ['collapse']}),
            ('Links', {'fields': ('link_slides',
              'link_maps',
            'mais_link',), 'classes': ['collapse']}),
            ('Valores', {'fields': ( 'valor',
            'consulta',
             'iptu'), 'classes': ['collapse']}),
            ('Informacoes_corretor', {'fields': ( 'observacoes_corretores', 
            'interessados',
             'idd'), 'classes': ['collapse']}),

             ]
    inlines = [ChoiceInline]

      #  ('Date information', {'fields': ['cidade'], 'classes': ['collapse']}),

admin.site.register(Imovei, QuestionAdmin)


class ChoiceInlinee(admin.TabularInline):
    model = Plantao
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
            ('.', {'fields': ( 'imagem', 
            'corretor',
            'numero_corretor',
            'email_corretor',
            'instagram_corretor',
            'facebook_corretor'), 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInlinee]
admin.site.register(Corretores, QuestionAdmin)






# só existe porque a gente quer que no admin apareça o campo personalizado filmes_vistos
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Histórico", {'fields': ('imoveis_vistos',)})
)

# Register your models here.
admin.site.register(Usuario, UserAdmin)