file_name = input("Введите имя файла: ")

with open(file_name,'r',encoding='utf-8') as f:
    for line in f:
        numbers = line.split()
        tatal =  0
        for num in numbers:
            tatal += int(num)
        print(tatal)