def length(x,y):
    if len(x)>len(y):
        print(x)
    elif len(x) == len(y):
        print(x,"\n",y)
    else:
        print(y)
a=input("Enter First String:")
b=input("Enter Second String:")   
length(a,b)