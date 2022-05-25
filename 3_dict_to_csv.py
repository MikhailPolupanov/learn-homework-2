"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv
def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    user_list = [
        {'Name': 'Михаил', 'Age': '31', 'Job': 'Реклама'},
        {'Name': 'Юлия', 'Age': '34', 'Job': 'Декретный отпуск'},
        {'Name': 'Тимофей', 'Age': '7', 'Job': 'Дошкольник'},
        {'Name': 'Ольга', 'Age': '61', 'Job': 'Врач'},
        {'Name': 'Григорий', 'Age': '63', 'Job': 'Пенсионер'},
        {'Name': 'Анна', 'Age': '39', 'Job': 'Предприниматель'},
        {'Name': 'Кира', 'Age': '10', 'Job': 'Школьник'},
        {'Name': 'Тихон', 'Age': '40', 'Job': 'Предприниматель'},
        {'Name': 'Ольга', 'Age': '60', 'Job': 'Пенсионер'},
        {'Name': 'Виктор', 'Age': '64', 'Job': 'Логист'}
    ]

    with open('export.csv', 'w', encoding='utf-8', newline='') as csv1:
        fields = ['Name', 'Age', 'Job']
        writer = csv.DictWriter(csv1, fields, delimiter=';')
        writer.writeheader()

        for row in user_list:
            writer.writerow(row)

    

if __name__ == "__main__":
    main()
