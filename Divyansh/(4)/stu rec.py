import pickle
myfile=open (r"student.dat", "wb")

stu1={"rollno" : 101, "name": "studentl", "Marks" : 90}
stu2={ "rollno" : 102, "name": "student2", "Marks": 56}
stu3={ "rollno" : 103, "name": "student3", "Marks" : 97}
stu4={ "rollno" : 104, "name": "student4", "Marks": 19}
stu5={ "rollno" : 105, "name": "student5", "Marks" : 95}
stu6={ "rollno" : 106, "name": "student6", "Marks" : 92}
stu7={ "rollno" : 107, "name": "student7", "Marks": 57}
stu8={ "rollno": 108, "name": "student8", "Marks" :99}

pickle.dump (stu1,myfile)
pickle.dump (stu2, myfile)
pickle.dump (stu3, myfile)
pickle.dump (stu4, myfile)
pickle.dump (stu5, myfile)
pickle.dump (stu6, myfile)
pickle.dump (stu7, myfile)
pickle.dump (stu8, myfile)

print ("succesful")
myfile.close ()
