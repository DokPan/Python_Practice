class Book:
    def __init__(self,name):
        self.__content__ =[]
        self.name =name
        print(f"Книга {name} создана")

    def __del__(self):
        print(f"Книга {self.name} удалена")

book1 = Book("Убийство бабки")
book2 = Book("Смерть Абобы")

del book1
del book2