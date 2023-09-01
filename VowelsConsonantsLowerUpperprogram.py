fp=open("VowelsConsonantsLowerUpper.txt","r")
r=fp.read()
vowels,consonants,upper_ch,lower_ch=0,0,0,0

for ch in r:
    if ch.islower():
        lower_ch+=1
    elif ch.isupper():
        upper_ch+=1
    if ch in ['a','e','i','o','u','A','E','I','O','U']:
        vowels+=1
    elif ch in ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']:
        consonants+=1
fp.close()

print("Vowels are : ",vowels)
print("Consonants are : ",consonants)
print("Lower case letters are : ",lower_ch)
print("Upper case letters are : ",upper_ch)
print(len(r))