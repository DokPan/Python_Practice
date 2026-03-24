books = {}

while True:
    print("1 - добавить 2 - удалить 3 - показать 4 - выход")
    c = input()

    if c == "1":
        books[input("название: ")] = input("автор: ")
    elif c == "2":
        try:
            del books[input("название: ")]
        except KeyError:
            print("Нет такой книги")
    elif c == "3":
        for k,v in books.items():
            print(k, "-", v)
    elif c == "4":
        break