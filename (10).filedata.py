
file = open('abc.txt', 'r') 
data = file.readlines() 
 
for i in data: 
    print(i.replace(" ", "#"))
