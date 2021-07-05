### part 1:::
def check_numbers(num1,num2):
        if num1%2==0 and num2%2==0:
            print("both are even numbers")
        else:
            print("both are not even numbers")
check_numbers(10,22)
check_numbers(1,15)
check_numbers(10,21)

### part 2:::
def check_numbers_list(num1,num2):
    i=0
    while i<len(num1):
        if num1[i]%2==0 and num2[i]%2==0:
            print("both are even numbers")
        else:
            print("both are not even numbers")
        i+=1
check_numbers_list([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87])