from django.contrib import admin

from .models import Servico, ProdutosServico


class ProdutoServicoInline(admin.TabularInline):
    model = ProdutosServico
    extra = 1

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'preco', 'get_produtos')
    inlines = [ProdutoServicoInline]
    search_fields = ('nome', 'descricao')

    def get_produtos(self, obj):
        return ', '.join([prd.produto.nome for prd in ProdutosServico.objects.filter(servico=obj.id)])

    get_produtos.short_description = 'Produtos utilizados'
