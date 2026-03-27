import json
import os

class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def get_name(self):
        return self.name

    def get_age(self):
        return int(self.age)

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
    print("\n1-Добавить 2-Просмотреть 3-Удалить 4-Сортировать 5-Выход")
    s = input()

    if s == "1":
        name = input("Имя: ")
        age = input("Возраст: ")
        while int(age) < 0:
            print("Возраст должен быть больше 0")
            age = input("Возраст: ")
        color = input("Окрас: ")
        cats.append(Cat(name, age, color))
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
        print("1-По имени 2-По возрасту")
        s = input()
        if s == "1":
            cats.sort(key=Cat.get_name)
        else:
            cats.sort(key=Cat.get_age)

    elif s == "5":
        data = []
        for c in cats:
            data.append({"name" : c.name, "age" : c.age, "color" : c.color})
            f = open("cats.json", "w", encoding="utf-8")
            json.dump(data, f, ensure_ascii=False)
            f.close()
        break