from random import*
import json


def load():
    with open ('D:\Code\Python\Lesson 4\data.json', 'r', encoding='utf-8') as f:
        global data
        data = json.load(f)

def save():
    with open("D:\Code\Python\Lesson 4\data.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False))
    print("Saved")

try:
    load()
except:
    data = []

while True:
    command = input("Введите команду: ")
    if command == "/all":
        print(data)
    elif command == "/help":
        print("Доступные команды: /all - посмотреть все записи /add - добавить /del - удалить /rnd - выбрать рандомную игру")
    elif command == "/add":
        add = input("Ввеедите название игры: ")
        data.append(add)
        save()
        print("Успешно добавлено")
    elif command == "/rnd":
        print(choice(data))
    elif command == "/del":
        rem = input("Введите название игры: ")
        try:
            data.remove(rem)
            save()
            print("Успешно удалено")
        except:
            print("Такой игры не найдено")
    elif command == "/stop":
        print("Бот остановил работу")
        break
    else:
        print("Неизвестная команда, введите /help для помощи")