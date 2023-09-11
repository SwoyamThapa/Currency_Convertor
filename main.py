import currency_name
import conversion
import currency_conversion

def main():

    country1 = input("Enter your first country:")
    country2 = input("Enter the second country: ")
    amount = float(input("Enter the amount you want to transfer: "))

    _curr1 = currency_name.Currency_name(country1)
    _curr2 = currency_name.Currency_name(country2)

    curr1 = _curr1.currency()
    curr2 = _curr2.currency()

    _conversion = currency_conversion.Currency_conversion(curr1,curr2,amount)
    _convert = _conversion.convert()

    if(curr1 == "not found" or curr2 == "not found"):
        print(f"{country1} and {country2} not found.")
        print("Enter again: ")
        print()
        main()
        
    
    if(curr1 == "not found"):
        print(f"{country1} not found.")
        print("Enter again: ")
        print()
        main()
    
    if(curr2 == "not found"):
        print(f"{country2} not found.")
        print("Enter again: ")
        print()
        main()

    if(_convert == "curr1 not found"):
        print(f"{country1} not found, ({country2} might me available).")
        print("Enter again: ")
        print()
        main()
    
    if(_convert == "curr2 not found"):
        print(f"{country2} not found.")
        print("Enter again: ")
        print()
        main()

    converted_amount = _convert * amount
    print(f"The conversion rate from {country1} to {country2} is 1{curr1} = {_convert}{curr2}")
    print(f"{amount}{curr1} = {converted_amount:.2f}{curr2}")

if __name__ == "__main__":
    main()