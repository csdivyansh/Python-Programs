t =input ("Enter a tuple: ")
tuple(t)
print(t)

search=input('Enter The Element you want index for: ')
index=0
counter=0
lt=len(t)
for x in range(lt): 
    if x==search:
        print(search+" is found at postion ")
        index=index+1
        print(index)
    else:
        print('Element not found')
