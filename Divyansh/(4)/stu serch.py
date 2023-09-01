import pickle
user=int(input("Enter roll no you want to search:"))
m=int(input("Update the marks"))

try:
    myfile=open (r"student.dat", "rb+")
    while True:
        temp=myfile.tell ()
        a=pickle.load (myfile)
        if a["rollno"]==user:
            myfile.seek (temp)
            a [ "Marks"]=m
            pickle.dump (a, myfile)
        print(a)
except FileNotFoundError:
    print ("please check the file name")
except EOFError :
    myfile . close ( )
