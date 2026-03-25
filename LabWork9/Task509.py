class Author:
    def __init__(self,f,s):
        self.f=f
        self.s=s
class Book:
    def __init__(self,name):
        self.__content__ =[]
        self.name =name
        print(f"Книга {name} создана")

    def add(self, creation):
        self.__content__.append(creation)


class BookAuthor(Author,Book):
    def __init__(self,f,s,name):
        Author.__init__(self,f,s)
        Book.__init__(self,name)

    def show(self):
        print(self.f,self.name,self.__content__)

bookAuthor=BookAuthor("Абоба Абобович Абобов -","АбобаЛенд","Смерть Абобы")

bookAuthor.add("Том 1: Абоба присмерти")
bookAuthor.add("Том 2: Абоба в печали")
bookAuthor.add("Том 3: Абоба умер")
bookAuthor.show()