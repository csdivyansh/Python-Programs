import csv
def write():
    f=open('unpw.csv','w',newline='')
    wo=csv.writer(f)
    wo.writerow(['Username','Passwords'])
    while True:
         u_id=input("Enter User ID: ")
         pswd=input("Enter Password: ")
         data=[u_id,pswd]
         wo.writerow(data)
         ch=input('Add more records?(y/n): ')
         if ch in 'Nn':
             break
    f.close()

def read():
    f=open('unpw.csv','r')
    ro=csv.reader(f)
    for i in ro:
        print(i)        
    f.close()

def search():
    f=open('unpw.csv','r')
    u=input('Enter user-id to search: ')
    found=0
    ro=csv.reader(f)
    next(ro)
    for i in ro:
        if i[0]==u:
                print('Password=',i[1])
                found=1
    f.close()
    if found==0:
        print('No record found')

write()
read()
search()         
