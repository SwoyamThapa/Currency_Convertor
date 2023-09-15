from forex_python.converter import CurrencyRates

class Conversion:

    def __init__(self, source_currency, target_currency, amount):

        self.source_currency = source_currency
        self.targer_currency = target_currency
        self.amount = amount

    def Conversion(self):
        currRatesObj = CurrencyRates()
        converted_amount = currRatesObj.convert(self.source_currency, self.target_currency, self.amount)
        
        return converted_amount

        
        