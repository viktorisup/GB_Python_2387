# Распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt

import requests

url = requests.get('https://raw.githubusercontent.com/elastic/examples/'
                  'master/Common%20Data%20Formats/nginx_logs/nginx_logs')
log_txt = url.text
with open('nginx_logs.txt', mode='wt', encoding='utf-8') as file:
    file.writelines(log_txt)
    with open('nginx_logs.txt', mode='rt', encoding='utf-8') as file1:
        lst = []
        for i in file1:
            ip = i.split('- -')[0].strip()
            tmp = i.split('"')[1]
            tp = tmp.split()[0]
            pt = tmp.split()[1]
            lst.append((ip, tp, pt))
        print(lst)
