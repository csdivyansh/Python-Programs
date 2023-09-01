def menu():
    print('What do you want to get:')
    print('1.Area of Circle')
    print('2.Area of Square')
    print('3.Area of Rectangle')
    global c
    c=int(input('Enter an option: '))
def ar_cir():
    r=int(input('Enter radius: '))
    A=(22/7)*r*r
    print('Area of circle = ',A)
def ar_sq():
    s=int(input('Enter side: '))
    A=s*s
    print('Area of square = ',A)
def ar_rec():
    l=int(input('Enter length: '))
    b=int(input('Enter breadth: '))
    A=l*b
    print('Area of rectangle = ',A)
menu()
if c==1:
    ar_cir()
elif c==2:
    ar_sq()
elif c==3:
    ar_rec()
else:
    print('Error')
    menu()
    
    
    
