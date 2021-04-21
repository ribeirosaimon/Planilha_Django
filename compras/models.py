from django.db import models
from django.contrib.auth import get_user_model



class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class CompraModel(Base):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    data = models.DateField()
    nacional = models.BooleanField()
    acao = models.CharField(max_length=10)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    preco_medio = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.acao