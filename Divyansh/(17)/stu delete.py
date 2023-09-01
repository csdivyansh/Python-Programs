import pickle
student={}
a=0

n=int(input("enter number of entries"))
for i in range(n):
    name=input("enter names")
    marks=eval(input("enter marks"))
    student[name]=marks
f=open("student.dat","wb")

x=input("enter rollno to be deleted")
for key in list(dict.keys(student)):
    if key==x:
        print(key)
        a= student[key].remove()

pickle.dump(a,f)
f.close()



