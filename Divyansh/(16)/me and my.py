def Cmemy():
    num=0
    fp=open('STORY.txt','r')
    count_me=count_my=0
    data=fp.read()
    words=data.split()    
    for i in words:
        if i=='me' or i=='Me':
            count_me+=1
        elif i=='my' or i=='My':
            count_my+=1
    a=count_me+count_my
    print('Count of Me/My in file: ',a)

Cmemy()
