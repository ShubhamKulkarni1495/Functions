def perfect():
    i=1
    sum=0
    while i<num:
        if num%i==0:
            sum+=i
        i+=1
    if num == sum:
        print("it is a perfect number")
    else:
        print("it is not perfect number")
num=int(input("enter a number:"))   
perfect()

def perfect():
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    if num == sum:
        print("it is a perfect number")
    else:
        print("it is not perfect number")
num=int(input("enter a number:"))   
perfect()

