

class Volatilidade():

    def __init__(self, dict_patrimonio, dias=0):
        self.dict_patrimonio = dict_patrimonio
        self.dias = dias


    def resposta_classe(self):
        return {
            'volatilidade_diaria':self.rentabilidade_diaria(),
            'volatilidade_anual':self.rentabilidade_diaria(anual=True),
            'volatilidade_media':self.rentabilidade_diaria(vol_media=True,qtd_dias=self.dias)
            }
        

    def rentabilidade_diaria(self, anual=False, vol_media=False, qtd_dias=0):
        dict_rent = {
            'rent_total':0,
            'rent_br':0,
            'rent_usa':0,
        }

        calc = self.dict_patrimonio['candle_total']['close'] - self.dict_patrimonio['candle_total']['open']
        calc_br = self.dict_patrimonio['candle_br']['close'] - self.dict_patrimonio['candle_br']['open']
        calc_usa = self.dict_patrimonio['candle_usa']['close'] - self.dict_patrimonio['candle_usa']['open']
        try:
            dict_rent['rent_total'] = round((calc / self.dict_patrimonio['candle_total']['open'])*100,4)
            dict_rent['rent_br'] = round((calc_br / self.dict_patrimonio['candle_br']['open'])*100,4)
            dict_rent['rent_usa'] = round((calc_usa / self.dict_patrimonio['candle_usa']['open'])*100,4)

            if vol_media == True:
                dict_rent['rent_total'] = round(((calc / self.dict_patrimonio['candle_total']['open']) * (self.dias ** 0.5)) *100,4)
                dict_rent['rent_br'] = round(((calc_br / self.dict_patrimonio['candle_br']['open']) * (self.dias ** 0.5))*100,4)
                dict_rent['rent_usa'] = round(((calc_usa / self.dict_patrimonio['candle_usa']['open']) * (self.dias ** 0.5))*100,4)
            
            if anual == True:
                dict_rent['rent_total'] = round(((calc / self.dict_patrimonio['candle_total']['open']) * (252 ** 0.5)) *100,4)
                dict_rent['rent_br'] = round(((calc_br / self.dict_patrimonio['candle_br']['open']) * (252 ** 0.5))*100,4)
                dict_rent['rent_usa'] = round(((calc_usa / self.dict_patrimonio['candle_usa']['open']) * (252 ** 0.5))*100,4)
        except:
            dict_rent['rent_total'], dict_rent['rent_br'], dict_rent['rent_usa'] = 0, 0, 0

        return dict_rent

