from django.db import models
from django.contrib.auth import get_user_model



class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class PatrimonioModel(Base):

    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    data = models.DateField()

    patrimonio_total = models.DecimalField(max_digits=10, decimal_places=2)
    patrimonio_br = models.DecimalField(max_digits=10, decimal_places=2)
    patrimonio_usa = models.DecimalField(max_digits=10, decimal_places=2)

    vol_total = models.DecimalField(max_digits=10, decimal_places=4)
    vol_br = models.DecimalField(max_digits=10, decimal_places=4)
    vol_usa = models.DecimalField(max_digits=10, decimal_places=4)

    def __str__(self):
        return f'{self.data}'