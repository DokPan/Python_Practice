n = int(input("Введите n (сек): "))

if 0 <= n <=(60*60*24-1):
    hours =0
    while (hours+1)*(60*60) <= n :
        hours = hours+1

    stock = n - (hours*(60*60))

    minutes = 0
    while (minutes+1)*60 <= stock :
        minutes = minutes+1

    seconds = stock - (minutes*60)
    print("{:02d}:{:02d}:{:02d}".format(hours,minutes,seconds))
else:
    print("ERROR")