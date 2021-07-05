def sum():
    x=[8,2,3,0,7]
    sum1=0
    for i in x:
        sum1=sum1+i
    print(sum1)
sum() 

def sum(x):
    sum1=0
    for i in x:
        sum1+=i
    return sum1
print(sum((8,2,3,0,7)))
