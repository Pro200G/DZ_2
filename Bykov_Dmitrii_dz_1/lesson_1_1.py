# a
dur = int(input('Введите время в секундах: '))
print(dur, 'сек')
#b
dur = int(input('Введите время в секундах: '))
if dur <= 59:
    print(dur, 'сек')
else:
    print(dur // 60, 'мин', dur % 60, 'сек')
#c
dur = int(input('Введите время в секундах: '))
if dur <= 59:
    print(dur, 'сек')
elif dur >= 60 and dur <= 3599:
    print(dur // 60, 'мин', dur % 60, 'сек')
else:
    print(dur // 3600, 'ч', dur // 60 % 60, 'мин', dur % 60, 'сек')
#d
dur = int(input('Введите время в секундах: '))
if dur <= 59:
    print(dur, 'сек')
elif dur >= 60 and dur <= 3599:
    print(dur // 60, 'мин', dur % 60, 'сек')
elif dur >= 3600 and dur <= 86399:
    print(dur // 3600, 'ч', dur // 60 % 60, 'мин', dur % 60, 'сек')
else:
    print(dur // 86400, 'дн', dur // 3600 % 24, 'ч', dur // 60 % 60, 'мин', dur % 60, 'сек')