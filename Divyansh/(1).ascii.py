def _ascii():
    c = input('Enter a character: ')
    if c.isdigit():           
        print("The ASCII value of '" + c + "' is",chr(int(c)))
    else:
        print("The ASCII code of '" + c + "' is", ord(c))
_ascii()
    



