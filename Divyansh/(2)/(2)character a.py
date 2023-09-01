fo=open("original.txt","w")
fo.write("Hi this is a text file I am making so it can remove all 'a'\nin the file and update this to a newer file.")
fo.close()
fo=open('original.txt','r')
fi=open('remove-a.txt','w')
l=fo.readlines()
for i in l:
    if 'a' in i:
        i=i.replace('a','')
        fi.write(i)
print('successful')
fi.close()
fo.close()
