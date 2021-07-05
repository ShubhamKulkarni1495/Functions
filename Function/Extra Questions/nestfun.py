def calcultor(operation):
    if operation == "add":
        def add(x,y):
            z=x+y
            print("Addition is:",z)
        a=int(input("ENter  number:"))
        b=int(input("ENter  number:"))
        add(a,b)
    if operation == "sub":
        def sub(x,y):
            z=x-y
            print("Subtraction is:",z)
        a=int(input("ENter  number:"))
        b=int(input("ENter  number:"))
        sub(a,b)
    if operation == "mul":
        def mul(x,y):
            z=x*y
            print("Multiplication is:",z)
        a=int(input("ENter  number:"))
        b=int(input("ENter  number:"))
        mul(a,b)
    if operation == "div":
        def div(x,y):
            z=x/y
            print("Division is:",z)
        a=int(input("ENter  number:"))
        b=int(input("ENter  number:"))
        div(a,b)
print("Helllo Welcome To Calculator:")   
cal=input("Which operation you want to perform:")
calcultor(cal)
