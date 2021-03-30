  
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView
from rest_framework.authtoken.models import Token
from django.urls import reverse_lazy
import requests
from django.conf import settings
from .forms import CompraModelForm
from django.contrib import messages

class CarteiraView(LoginRequiredMixin, FormView):
    login_url = 'user/login/'
    redirect_field_name = 'index'
    template_name = 'index.html'
    form_class = CompraModelForm
    success_url = reverse_lazy('relatorio_carteira')

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

    def form_valid(self,form,*args,**kwargs):
        acao = form.save(commit=False)
        acao.usuario = self.request.user
        acao.save()
        messages.success(self.request, 'Ação salva')
        return super(CarteiraView, self).form_valid(form,*args,**kwargs)

    def form_invalid(self, form, *args3, **kwargs):
        messages.error(self.request,'Algo deu errado')
        return super(CarteiraView, self).form_valid(form,*args,**kwargs)

def dict_contexto(dicionario):
    acao = list(dicionario.keys())[0]
    dict_retorno = {
        'acao':acao,
        'nacional':dicionario[acao]['nacional'],
        'pm':dicionario[acao]['pm'],
        'qtd':dicionario[acao]['qtd'],
        'pos':dicionario[acao]['pos'],
        'lucro':dicionario[acao]['lucro'],
        'preco_acao':dicionario[acao]['preco_acao']
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
        return context


class RelatorioImpostoRenda(LoginRequiredMixin, TemplateView):
    login_url = 'user/login/'
    redirect_field_name = 'relatorio_ir'
    template_name = 'relatorio_ir.html'

    def get_context_data(self, **kwargs):
        nome_user = self.request.user
        token = Token.objects.get(user=nome_user)
        context = super(RelatorioImpostoRenda, self).get_context_data(**kwargs)
        url = f'{settings.URL_BASE}/api/v1/relatorio/venda'
        headers = {'Authorization': f'Token {token}'}
        carteira = requests.get(url, headers=headers).json()
        context['ir'] = carteira
        return context  