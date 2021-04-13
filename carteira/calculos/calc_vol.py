class Volatilidade():

    def __init__(self, dict_patrimonio):
        self.dict_patrimonio = dict_patrimonio


    def resposta_classe(self):
        return {
            'volatilidade_diaria':self.rentabilidade_diaria(),
            'volatilidade_anual':self.rentabilidade_diaria(anual=True)
            }
        

    def rentabilidade_diaria(self, anual=False):
        dict_rent = {
            'rent_total':0,
            'rent_br':0,
            'rent_usa':0,
        }

        calc = self.dict_patrimonio['candle_total']['close'] - self.dict_patrimonio['candle_total']['open']
        calc_br = self.dict_patrimonio['candle_br']['close'] - self.dict_patrimonio['candle_br']['open']
        calc_usa = self.dict_patrimonio['candle_usa']['close'] - self.dict_patrimonio['candle_usa']['open']
        
        dict_rent['rent_total'] = round(calc / self.dict_patrimonio['candle_total']['open']*100,4)
        dict_rent['rent_br'] = round(calc / self.dict_patrimonio['candle_br']['open']*100,4)
        dict_rent['rent_usa'] = round(calc / self.dict_patrimonio['candle_usa']['open']*100,4)
        
        if anual == True:
            dict_rent['rent_total'] = round(((calc / self.dict_patrimonio['candle_total']['open']) * (252 ** 0.5)) *100,4)
            dict_rent['rent_br'] = round(((calc / self.dict_patrimonio['candle_br']['open']) * (252 ** 0.5))*100,4)
            dict_rent['rent_usa'] = round(((calc / self.dict_patrimonio['candle_usa']['open']) * (252 ** 0.5))*100,4)

        return dict_rent