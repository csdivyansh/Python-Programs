import pickle

def write():
    stu= {}
    stufile = open('Stu.dat', 'wb')
    ans = 'y'
    while ans == 'y' :
        rno = int(input ("Enter roll number: "))
        name=input("Enter name: ")
        marks=float(input("Enter marks: "))
        stu['Rollno'] = rno
        stu['Name'] = name
        stu[ 'Marks'] = marks
        pickle.dump(stu,stufile)
        ans = input("Want to enter more records? (y/n)...")
    stufile.close()

def search():
    f = open("reco.dat","rb")
    while True:
        text = pickle.load(stufile)
        try:
            if text["Rollno"] == rno:
                print("Search result:")
                print("Roll no: ",text['Roll no.'])
                print("Name: ",text['Name'])
                break
        except EOFError:
            print("Roll no. not found!")
            break
        stufile.close()
x=input()
if x==1:
    write()
elif x==2:
    search()
else:
    x
