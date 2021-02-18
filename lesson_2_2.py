weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
text_changes = []
for list_weather in weather:
    if list_weather.replace('+', '').isdigit():
        if list_weather[0] == '+':
            text_changes.append(f"'{list_weather[0] + '0' + list_weather[1:]}")
        else:
            text_changes.append(f"'0{list_weather}'")
    else:
        text_changes.append(list_weather)

print(" ".join(text_changes))