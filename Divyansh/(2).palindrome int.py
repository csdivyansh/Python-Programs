def pdnum():
    
    n=int(input("Enter a number to check its palindrome or not: "))
    num=str(n)
    
    rev=num[::-1]
    
    if (num==rev):
        print(True)
    else:
        print(False)
    pdnum()
    
pdnum()
        
        
