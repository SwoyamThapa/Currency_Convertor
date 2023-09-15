import requests

class Currency_conversion:

    def __init__(self, base_currency, target_currency, amount) -> None:
        self.base_currency = base_currency
        self.target_currency = target_currency
        self.amount = amount


    def convert(self):
        api_key = 'd75582718ec3b2f1f371b78b' 
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{self.base_currency}"
        # Replace with your actual API key
        headers = {'apikey': api_key}

        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
        
        # Extract the exchange rate from the response
            exchange_rates = data['conversion_rates']

            if(self.target_currency in exchange_rates):
                exchange_rate = data['conversion_rates'][self.target_currency]
                return exchange_rate
            else:
                return "curr2 not available"
        else:
            return "curr1 not available"

    
    
        