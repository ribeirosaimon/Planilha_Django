  
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from rest_framework.authtoken.models import Token
import requests
from django.conf import settings


class CarteiraView(LoginRequiredMixin, TemplateView):
    login_url = 'user/login/'
    redirect_field_name = 'index'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        nome_user = self.request.user
        token = Token.objects.get(user=nome_user)
        context = super(CarteiraView, self).get_context_data(**kwargs)
        url = f'{settings.URL_BASE}/api/v1/carteira/'
        headers = {'Authorization': f'Token {token}'}
        carteira = requests.get(url, headers=headers).json()
        context['info'] = carteira
        context['carteira'] = [dict_contexto(x) for x in carteira['carteira'] if list(x.keys())[0] != 'caixa']
        return context


def dict_contexto(dicionario):
    acao = list(dicionario.keys())[0]
    dict_retorno = {
        'acao':acao,
        'nacional':dicionario[acao]['nacional'],
        'pm':dicionario[acao]['pm'],
        'qtd':dicionario[acao]['qtd'],
        'pos':dicionario[acao]['pos'],
        'lucro':dicionario[acao]['lucro'],
    }
    return dict_retorno


class AnaliseTecnicaView(LoginRequiredMixin, TemplateView):
    login_url = 'user/login/'
    redirect_field_name = 'analise_tecnica'
    template_name = 'analise_tecnica.html'

    def get_context_data(self, **kwargs):
        nome_user = self.request.user
        token = Token.objects.get(user=nome_user)
        context = super(AnaliseTecnicaView, self).get_context_data(**kwargs)
        url = f'{settings.URL_BASE}/api/v1/relatorio/carteira'
        headers = {'Authorization': f'Token {token}'}
        carteira = requests.get(url, headers=headers).json()['carteira']
        info_carteira = [{'acao':list(x.keys())[0],'info':list(x.values())[0]} for x in carteira if list(x.keys())[0] != 'caixa']
        context['info']= info_carteira
        print(info_carteira)
        return context