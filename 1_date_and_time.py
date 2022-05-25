"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import date, datetime, timedelta
def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    dt_now = datetime.now()
    delta_yes = dt_now - timedelta(days=1)
    delta_mon = dt_now - timedelta(days=30)
    print(f'Вчера: {delta_yes.strftime("%d.%m.%Y")}')
    print(f'Сегодня: {dt_now.strftime("%d.%m.%Y")}')
    print(f'30 дней назад: {delta_mon.strftime("%d.%m.%Y")}')
    



def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    
    """
    date_string = "01/01/20 12:10:03.234567"
    date_time = datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")
    return date_time
    

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
