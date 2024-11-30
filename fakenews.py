from datetime import datetime, timedelta
def choose_plural(am, dec):
    if len(str(am)) > 1 and int(str(am)[-2:]) > 9 and  int(str(am)[-2:]) < 20:
        return f'{am} {dec[2]}'
    elif str(am)[-1:] == '1':
        return f'{am} {dec[0]}'
    elif str(am)[-1] in ['2', '3', '4']:
        return f'{am} {dec[1]}'
    else:
        return f'{am} {dec[2]}'
dt = datetime.strptime(input(), '%d.%m.%Y %H:%M')
dtvupysk = datetime(day=8, month=11, year=2022, hour=12)
raz = dtvupysk - dt
if raz > timedelta(seconds=0):
    if raz.days:
        print(f'До выхода курса осталось: {choose_plural(raz.days, ("день", "дня", "дней")) if raz.days else ""}{" и " if  raz.seconds // 3600 and raz.days else ''}{choose_plural(raz.seconds // 3600, ("час", "часа", "часов")) if raz.seconds else ""}')
    else:
        print(f'До выхода курса осталось: {choose_plural(raz.seconds // 3600, ("час", "часа", "часов")) if raz.seconds // 3600 else ""}{" и " if  raz.seconds // 3600 and raz.seconds % 3600 // 60 else ''}{choose_plural(raz.seconds % 3600 // 60, ("минута", "минуты", "минут")) if raz.seconds % 3600 // 60 else "" }')
else:
    print('Курс уже вышел!')
