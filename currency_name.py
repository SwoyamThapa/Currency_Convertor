import pycountry

class currency_name:

    def __init__(self, country_name) -> None:
        self.country_name = country_name

    def currency(self):
        _country = pycountry.countries.get(name=self.country_name)

        if _country:
            _currency = pycountry.currencies.get(numeric=country.numeric)
            if _currency:
                return _currency.alpha_3
            else:
                return "no_currency"
        else:
            return "no_country"

        
