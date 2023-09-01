myfile=open("answer.txt","r")
ch=" "
vcount=0
ccount=0
while ch:
    ch=myfile.readline(1)
    if ch in ['a','e','i','o','u','A','E','I','O','U']:
        vcount=vcount+1
    else:
        ccount=ccount+1
print("Vowels:",vcount)
print("Consonants:",ccount)
myfile.close()
