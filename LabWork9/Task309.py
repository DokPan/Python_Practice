class Book:
    def __init__(self,name):
        self.__content__ =[]
        self.name =name
        print(f"Книга {name} создана")

    def __del__(self):
        print(f"Книга {self.name} удалена")

    def add(self,creation):
        self.__content__.append(creation)

    def count(self):
        return len(self.__content__)

book2 = Book("Смерть Абобы")

book2.add("Том 1: Абоба присмерти")
book2.add("Том 2: Абоба в печали")
book2.add("Том 3: Абоба умер")

print(f"Количество произведений: {book2.count()}")
