from relatorio_carteira.models import PatrimonioModel
from carteira.calculos.calc_vol import Volatilidade
from datetime import date
from decimal import Decimal

def salvar_em_banco(info, user, candle_carteira):
    vol = Volatilidade(candle_carteira).resposta_classe()


    data_atual = date.today()
    patrimonio_total = info['patrimonio']['patrimonio_total']['pos']
    patrimonio_br = info['patrimonio']['patrimonio_br']['pos']
    patrimonio_usa = info['patrimonio']['patrimonio_usa']['pos']

   
    vol_total = round(Decimal(vol['volatilidade_diaria']['rent_total']),4)
    vol_br = Decimal(vol['volatilidade_diaria']['rent_br'])
    vol_usa = Decimal(vol['volatilidade_diaria']['rent_usa'])


    patrimonio = PatrimonioModel.objects.order_by('criacao')

    if len(patrimonio) == 0:
        salvar_patrimonio(user, data_atual, patrimonio_total, patrimonio_br, patrimonio_usa, vol_total, vol_br, vol_usa)

    try:
        if patrimonio[0].data != data_atual:
            salvar_patrimonio(user, data_atual, patrimonio_total, patrimonio_br, patrimonio_usa, vol_total, vol_br, vol_usa)
            
        if patrimonio[0].data == data_atual:
            patr_model = PatrimonioModel.objects.filter(data=data_atual).first()

            patr_model.patrimonio_total = patrimonio_total
            patr_model.patrimonio_br = patrimonio_br
            patr_model.patrimonio_usa = patrimonio_usa

            patr_model.vol_total = vol_total
            patr_model.vol_br = vol_br
            patr_model.vol_usa = vol_usa

            patr_model.save()
    except:
        print('Deu algum problema')


def salvar_patrimonio(user, data_atual, patrimonio_total, patrimonio_br, patrimonio_usa, vol_total, vol_br, vol_usa):
    patrimonio_obj = PatrimonioModel(
    usuario = user,
    data=data_atual,
    patrimonio_total=patrimonio_total,
    patrimonio_br=patrimonio_br,
    patrimonio_usa=patrimonio_usa,
    vol_total=vol_total,
    vol_br=vol_br,
    vol_usa=vol_usa
    )
    patrimonio_obj.save()