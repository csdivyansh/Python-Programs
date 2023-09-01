import pickle
myfile=open (r"student.dat", "wb+")
a={}
found=False
n=int(input('How many students?: '))
for i in range (n) :
    roll=int (input ("Enter the rollno: ") )
    name=input ("Enter the name: ")
    a ["roll"]=roll
    a ["name"]=name
    pickle.dump (a, myfile)

myfile.seek (0)
c=int (input ("enter the roll no to search: ") )

try :
    while True:
        b=pickle.load (myfile)
        if b["roll"]==c:
            print (b)
            found=True
except EOFError :
    if found:
        myfile.close ()
    else:
        print ("student details not found")
        myfile.close()
