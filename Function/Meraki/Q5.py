# ### part 1:::
# def calculator(number_x, number_y,operation1):
#     if operation1=="add":
#         add1=number_x+number_y
#         return add1
#     if operation1=="sub":
#         sub1=number_x-number_y
#         return sub1
#     if operation1=="mul":
#         mul1=number_x*number_y
#         return mul1
#     if operation1=="div":
#         div1=number_x/number_y
#         return div1
# x=int(input("enter first number:"))
# y=int(input("enter second number:"))
# z=input("Enter the operation you want to perform:")
# result=calculator(x,y,z)
# print(result)


### part 2:::
def list_change(x,y):
    i=0
    new_list=[]
    while i<len(x):
        z=x[i]*y[i]
        new_list.append(z)
        i+=1
    return new_list
multiple_list = list_change([5, 10, 50, 20], [2, 20, 3, 5]) 
print(multiple_list)