fp=open('abc.txt','r')

count_to=0
count_the=0
data=fp.read()
words=data.split()

for i in words:
    if i=='to':
        count_to+=1
    elif i=='the':
        count_the+=1
print(words)
print('No of words = ',len(words))
print('No of to(s) = ',count_to)
print('No of the(s) = ',count_the)

