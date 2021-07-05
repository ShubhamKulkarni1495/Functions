def even(x):
    y=[]
    for i in x:
        if i%2==0:
            y.append(i)
        else:
            pass
    print(y)
even(((1, 2, 3, 4, 5, 6, 7, 8, 9)))

def odd(x):
    y=[]
    for i in x:
        if i%2!=0:
            y.append(i)
        else:
            pass
    print(y)
odd(((1, 2, 3, 4, 5, 6, 7, 8, 9)))


def even(x):
    y=[]
    i=0
    while i<len(x):
        if x[i]%2==0:
            y.append(x[i])
        else:
            pass
        i+=1
    print(y)
even(((1, 2, 3, 4, 5, 6, 7, 8, 9)))

def odd(x):
    y=[]
    i=0
    while i<len(x):
        if x[i]%2!=0:
            y.append(x[i])
        else:
            pass
        i+=1
    print(y)
odd(((1, 2, 3, 4, 5, 6, 7, 8, 9)))