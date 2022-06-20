# Написать функцию currency_rates(), принимающую в качестве аргумента
# код валюты (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.

import requests

url = 'http://www.cbr.ru/scripts/XML_daily.asp'

def currency_rates(url, val):
    url1 = requests.get(url)
    url_content = url1.text
    val = val.upper()
    if val in url_content:
        valute = url_content.split(val)
        value = valute[1].split('<Value>')[1].split('</Value>')[0]
        value = float(value.replace(',', '.'))
        return value
    else:
        return None

print(currency_rates(url, 'usd'))
print(currency_rates(url, 'eUr'))
print(currency_rates(url, 'cnY'))
print(currency_rates(url, 'u11'))
