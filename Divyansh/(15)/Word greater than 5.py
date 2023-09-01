def BIGWORDS():
    fp=open('CODE.txt','r')
    o=fp.read()
    str5=0
    text = o.split()
    for x in text:
        if len(x) > 5:
            str5+=1
    print('Count of big words:',str5)
    
BIGWORDS()

