def duplicate(x):
    y=[]
    for i in x:
        if i not in y:
            y.append(i)
        else:
            pass
    print(y)
duplicate(((1,2,3,3,3,3,4,5)))

def duplicate(x):
    y=[]
    i=0
    while i<len(x):
        if x[i] not in y:
            y.append(x[i])
        else:
            pass
        i+=1
    print(y)
duplicate(((1,2,3,3,3,3,4,5)))