def fact(x):
    if x==0:
        return 1
    else:
        return x*fact(x-1)
print(fact(5))

def fact():
    fac=1
    i=1
    while i<=x:
        fac=fac*i
        i+=1
    print(fac)
x=int(input("enter a number:"))
fact()