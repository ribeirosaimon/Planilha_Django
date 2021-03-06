from django.db import models
from django.contrib.auth import get_user_model



class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class VendaModel(Base):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    data = models.DateField()
    nacional = models.BooleanField()
    acao = models.CharField(max_length=10)
    quantidade = models.IntegerField()
    preco_medio = models.DecimalField(max_digits=10, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    dolar = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)


    def __str__(self):
        return self.acao