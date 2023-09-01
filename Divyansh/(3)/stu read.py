import pickle
f=open('student.dat','rb')
s=pickle.load(f)
print(s)
