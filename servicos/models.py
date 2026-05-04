from django.db import models


class Servico(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=100, help_text='Nome completo do serviço', unique=True)
    preco = models.DecimalField(verbose_name='Preço', max_digits=5, decimal_places=2, help_text='Preço do serviço')
    descricao = models.TextField(verbose_name='Descrição', max_length=300,
                                 help_text='Descrição e observações do serviço')

    produtos = models.ManyToManyField(to='produtos.Produto', through='servicos.ProdutosServico',
                                      related_name='servico_produtos')

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.nome


class ProdutosServico(models.Model):
    servico = models.ForeignKey(to='servicos.Servico', verbose_name='Serviço', on_delete=models.CASCADE,
                                related_name='produtos_servico_servico')
    produto = models.ForeignKey(to='produtos.Produto', verbose_name='Produto', on_delete=models.PROTECT,
                                related_name='produtos_servico_produto')
    quantidade = models.DecimalField(verbose_name='Quantidade', max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'Produto utilizado'
        verbose_name_plural = 'Produtos utilizados'

    def __str__(self):
        return f'{self.produto}'