import json
import os

class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

if os.path.exists("cats.json"):
    f = open("cats.json", "r", encoding="utf-8")
    data = json.load(f)
    f.close()
    cats = []
    for c in data:
        cats.append(Cat(c["name"], c["age"], c["color"]))
else:
        cats = []

while True:
    print("\n1-Добавить 2-Просмотреть 3-Удалить 4-Выход")
    s = input()

    if s == "1":
        cats.append(Cat(input("Имя: "), input("Возраст: "), input("Окрас: ")))
        print("Кот добавлен")

    elif s == "2":
        if len(cats) == 0:
            print("Котов нет")
        else:
            for c in cats:
                print(c.name, c.age, c.color)

    elif s == "3":
        name = input("Имя: ")
        new_cats = []
        for c in cats:
            if c.name != name:
                new_cats.append(c)
        cats = new_cats
        print("Кот удален")

    elif s == "4":
        data = []
        for c in cats:
            data.append({"name" : c.name, "age" : c.age, "color" : c.color})
            f = open("cats.json", "w", encoding="utf-8")
            json.dump(data, f, ensure_ascii=False)
            f.close()
        break