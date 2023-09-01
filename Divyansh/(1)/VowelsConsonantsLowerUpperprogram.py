fp=open("VowelsConsonantsLowerUpper.txt","r")
r=fp.read()
vow,con,upper_ch,lower_ch=0,0,0,0
for i in r:
    if i.isalpha():
        if i in ['a','e','i','o','u','A','E','I','O','U']:
            vow+=1
        else:
            con+=1
    if i.islower():
        lower_ch+=1
    elif i.isupper():
        upper_ch+=1
fp.close()
print("Vowels are : ",vow)
print("Consonants are : ",con)
print("Lower case letters are : ",lower_ch)
print("Upper case letters are : ",upper_ch)


