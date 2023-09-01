fp=open('abc.txt','r')
data=fp.read()
words=data.split()
print(words)
rem=input('Enter a word to remove: ')
for i in words:
    if rem in words:
        words.remove(rem)
print(words)
fp.close()
    

