# OOP Project
# currency converter
# simple solution, no GUI

import requests


class Converter:
    def __init__(self):
        with open('currencies.txt', 'r') as a:
            self.currencies = a.read().replace('\n', '').split(',')

    def list_currencies(self):
        """List all available currencies"""
        print(", ".join(self.currencies))

    def check_currency(self, currency):
        """Check if currency is availabe for conversion. Use code (USD)."""
        if currency.upper() in self.currencies:
            return True
        else:
            return False

    def convert_value_of(self, base_currency, converted_currency, amount=1.0):
        """Convertion function"""
        if base_currency.upper() in self.currencies and converted_currency.upper() in self.currencies:
            url = f'https://api.exchangerate-api.com/v4/latest/{base_currency.upper()}'
            curr = requests.get(url).json()
            rate = curr['rates'][converted_currency.upper()]
            return amount * rate
        else:
            return 'Currency not valid'


if __name__ == "__main__":
    c = Converter()

    while True:
        str_base_currency = str(input('What is the base currency? ')).upper()
        if len(str_base_currency) == 3 and str_base_currency in c.currencies:
            break
        else:
            print('Please use the 3 digit code for the currency')

    while True:
        str_converted_currency = str(input('What is the currency you to convert to? ')).upper()
        if len(str_converted_currency) == 3 and str_converted_currency in c.currencies:
            break
        else:
            print('Please use the 3 digit code for the currency')

    while True:
        try:
            flt_amount = float(input('What is the amount you want to convert? '))
            break
        except ValueError:
            print('Please insert numbers.')

    result = c.convert_value_of(str_base_currency, str_converted_currency, flt_amount)
    if result == 'Currency not valid':
        print(result)
    else:
        print(f'{flt_amount:.2f} unit(s) of {str_base_currency.upper()} equals {result:.2f} unit(s) of {str_converted_currency.upper()}')

