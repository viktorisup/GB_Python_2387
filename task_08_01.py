# Написать функцию 'email_parse(<email_address>)', которая при помощи регулярного
# выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря.
import re

def email_parse(email):
    re1 = re.compile('(?P<users>^\w+[^=*&^%$#>@A-z]?\w*)@(?P<domain>[\w-]+\.[a-z]{2,6}(\.[a-z]{2,6})?)')
    try:
        rez = re1.search(email)
        return rez.groupdict()
    except (AttributeError, ValueError):
        print('Неверный емаил:', email)

print(email_parse('user0_name@domenname.ru'))
print(email_parse('user2.name@domenname.ru'))
print(email_parse('user3+name@domenname.ru'))
print(email_parse('user4-name@domenname.ru'))
print(email_parse('user12_name@domenna.me.ru'))
