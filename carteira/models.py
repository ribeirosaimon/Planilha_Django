from django.db import models
from django.contrib.auth import get_user_model



class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class CarteiraModel(Base):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)