def check(x):
    i=1
    while i<=x:
        if i%3==0 or i%5==0:
            print(i)
        i+=1
x=int(input("Enter the range:"))
check(x)