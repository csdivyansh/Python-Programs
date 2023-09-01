lst_1=input('Enter List_1 items: ').split()
lst_2=input('Enter List_2 items: ').split()
lst_3=input('Enter List_3 items: ').split()
lst_1.extend(lst_3)
lst_1[::-1]
lst_1.extend(lst_2)
print(lst_1)
