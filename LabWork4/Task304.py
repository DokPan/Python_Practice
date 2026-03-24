list1=[1,2,3,4,5]
list2 = [6,7,8,9,10]
for i in range(len(list2)):
    if list2[i]%2 == 0:
        list1.append(list2[i])
    else:
        pass

print(list1)