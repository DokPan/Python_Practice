a = int(input("Введите сумму: "))
b = int(input("Внесенная сумма: "))
while a !=b:
    if a <= 0:
        print("Введите сумму покупки:")
        a = int(input())
    elif b < a:
        print("Не хватает денег")
        print(f"Не хватает {a-b}")
        print("Внесите ещё денег:")
        b += int(input())
    elif b >a:
        print(f"Возмите сдачу,{b-a}")
        b -= b-a

print("Спасибо за покупку")

