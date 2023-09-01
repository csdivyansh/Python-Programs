def longestLength(a):
    max = len(a[0])
    temp = a[0]
    for i in a:
        if (len(i) > max):
            max = len(i)
            temp = i
    print("The longest word is:", temp)
    print("length= ", max)

a = ['Hi', 'This','is','a','list','Haloalkanes']
longestLength(a)
