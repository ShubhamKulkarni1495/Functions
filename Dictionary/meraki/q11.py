dic= {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
list1=[]
fm=0
sm=0
tm=0
for i in dic:
    for j in dic:
        if dic[j]>fm:
            fm=dic[j]
        if fm>dic[j] and dic[j]>sm:
            sm=dic[j]
        if sm>dic[j] and dic[j]>tm:
            tm=dic[j]
list1.append(fm)
list1.append(sm)
list1.append(tm)
print(list1)

