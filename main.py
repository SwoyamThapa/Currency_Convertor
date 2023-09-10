import currency_name
import conversion
import currency_conversion

def main():

    country1 = 'United States'
    country2 = 'Canada'
    amount = 1


    curr1 = currency_name.Currency_name(country1)
    curr2 = currency_name.Currency_name(country2)

    _conversion = currency_conversion.Currency_conversion(curr1.currency(),curr2.currency(),amount)

    _conversion.convert()

if __name__ == "__main__":
    main()