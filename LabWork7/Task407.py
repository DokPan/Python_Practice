def multiply_list(list,num=-1):
    for i in range(len(list)):
        list[i]*=num
    print(list)

a=[1,2,3,4,5]
multiply_list(a,2)

b=[1,2,3,4,5]
multiply_list(b)
