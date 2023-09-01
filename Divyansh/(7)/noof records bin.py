import pickle
file = open("STUDENT.DAT","rb")
count = 0
try:
    while True:
        record = pickle.load(file)
        if record['Marks'] > 0:
            count+=1
except EOFError:
    pass
print('No of records = ', count)
file.close()

