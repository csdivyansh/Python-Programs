import random
def Dice():
    ans='y'
    while ans=='y':
        r=random.randint(1,6)
        print(r)
        ans=input('Roll the dice again?(y/n): ')
Dice()
