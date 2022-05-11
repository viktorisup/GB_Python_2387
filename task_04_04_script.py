from task_04_04_utils import currency_rates as cr

print(cr('http://www.cbr.ru/scripts/XML_daily.asp', 'usd'))
print(cr('http://www.cbr.ru/scripts/XML_daily.asp', 'EUR'))
print(cr('http://www.cbr.ru/scripts/XML_daily.asp', 'usc'))