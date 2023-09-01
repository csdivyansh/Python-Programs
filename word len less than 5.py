def less_5(k, str):
    string = []
    text = str.split(" ")
    for x in text:
        if len(x) < k:
            string.append(x)
    return string

fp=open('abc.txt','r')
k = 5
str =fp.read()
print(less_5(k, str))
