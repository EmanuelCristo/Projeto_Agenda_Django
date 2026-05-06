import random

from django.core.management import BaseCommand
from django_seed import Seed

from produtos.models import Produto
from servicos.models import ProdutosServico, Servico


class Command(BaseCommand):
    help = 'Seed customizada para gerar dados para produtos utilizados em serviços'

    def handle(self, *args, **kwargs):
        seeder = Seed.seeder()
        seeder.add_entity(ProdutosServico, 40, {
            'servico': lambda x: random.choice(Servico.objects.all()),
            'produto': lambda x: random.choice(Produto.objects.all()),
            'quantidade': lambda x: random.uniform(0.01, 100.100),
        })

        inserted_pks = seeder.execute()

        self.stdout.write(self.style.SUCCESS(f'Instâncias de Produtos utilizados em Serviços foram criadas'))