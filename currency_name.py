import pycountry

class Currency_name:

    def __init__(self, country_name) -> None:
        self.country_name = country_name

    def currency(self):
        _country = pycountry.countries.get(name=self.country_name)

        if _country:
            _currency = pycountry.currencies.get(numeric=_country.numeric)
            if _currency:
                return _currency.alpha_3
            else:
                return "not found"
        else:
            return "not found"

        
