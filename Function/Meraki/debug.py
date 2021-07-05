# ### debug 1:::
# def sum():
#     print(12+13)
# sum() 

# ### debug 2:::
# def welcome():
#     print("Welcome to function")
# welcome() 

# ### debug 3:::
# def isEven():
#     if(12%2==0):
#         print("Even Number")
#     else:
#         print("Odd Number") 
# isEven()

# ### debug 4:::
# def greet(*names):
#     for name in names:
#         print("Welcome", name)

# greet("Rinki", "Vishal", "Kartik", "Bijender") 

# ### debug 5:::
# def info(name, age=0):
#    print(name, " is ", age ," years old")

# info("Sonu")
# info("Sana", "17")
# info("Umesh", "18") 

# ### debug 6:::

# def studentDetails(name,currentMilestone,mentorName):
#     print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ", mentorName)
# studentDetails("Nilam","loop","Abhishek") 

### debug 7:::
def calculate_sum(a,b):
    sum = a+b
    print(sum)
calculate_sum(4,5)

### debug 8:::
def multi(a,b):
    multi=a*b
    return multi
print(multi(3,4)) 

### debug 9:::
def Avg(number1,number2,number3):
    sum=number1+number2+number3
    avg=sum/3
    print(avg)
Avg(1,3,2)

### debug 10:::
def voter(age):
    if age < 18:
        print("eligible")
    else:
        print("not eligible")
voter(20)

### debug 11:::
 
def distance(kms):
        if kms < 20:
            print("close")
        elif kms < 50:
            print("medium")
        else:
            print("fast")
distance(70) 