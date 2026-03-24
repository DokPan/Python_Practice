mlist=[60,89,90,100,75,60,89,100,98,100,75,82]
rlist=[60,89,90,100,75,60,89,100,98,100,75,82]
ilist=[60,89,90,100,75,60,89,100,98,100,75,82]

nlist = ["Катя","Андрей","Виктор","Александр","Виталя","Оля",
         "Фрося", "Катя","Андрей","Виктор","Оля","Фрося"]
students =[]
for i in range (len(nlist)):
    tatal = mlist[i]+rlist[i]+ilist[i]
    students.append([tatal,nlist[i]])
    students.sort(reverse=True)
for i in range (10):
    print(f"{i+1}:{students[i][1]} сумма = {students[i][0]}")