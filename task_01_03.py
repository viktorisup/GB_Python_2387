# Реализовать склонение слова «процент» во фразе «N процентов».
phrase = 102
cnt = 0
while cnt < phrase:
    if (cnt % 10 == 0 or cnt == 11 or cnt == 12 or cnt == 13 or cnt == 14 or 4 < cnt % 10 <= 9):
        print(cnt, 'процентов')
    elif 2 <= cnt % 10 < 5:
        print(cnt, 'процента')
    elif cnt % 10 == 1:
        print(cnt, 'процент')
    cnt += 1