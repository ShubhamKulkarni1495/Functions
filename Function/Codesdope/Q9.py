def prime(x):
    if x>1:
        for i in range(2,x):  
            if x%i==0:
                print("Its not a prime number")
                break
        else:
            print("Its a prime number")
    else:
        print("Its not a prime number")
a=int(input("ENter the number:"))
prime(a)
