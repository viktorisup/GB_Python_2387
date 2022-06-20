#Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах.

second = 1
minute = 60
hour = 3600
day = 86400

while True:
    duration = int(input('Введите число в секундах: '))
    result_day = duration // day
    result_hour = (duration % day) // hour
    result_minute = ((duration % day) % hour) // minute
    result_second = (((duration % day) % hour) % minute) // second

    if result_day == 0 and result_hour == 0 and result_minute == 0:
        print(result_second, 'сек')
    elif result_day == 0 and result_hour == 0:
        print(result_minute, 'мин', result_second, 'сек')
    elif result_day == 0:
        print(result_hour, 'час', result_minute, 'мин', result_second, 'сек')
    else:
        print(result_day, 'дн', result_hour, 'час', result_minute, 'мин', result_second, 'сек')