import requests
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
