percent = 0
for percent in range(1, 21):
    if percent == 1:
        print(percent, 'процент')
    elif percent >= 2 and percent <= 4:
        print(percent, 'процента')
    elif percent >= 5 and percent <= 20:
        print(percent, 'процентов')