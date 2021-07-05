### part 1:::
def add_numbers(num1,num2):
    print(num1+num2)
add_numbers(56,12)

### part 2:::
def add_number_list(num1,num2):
    i=0
    while i<len(num1) or i<len(num2):
        sum=num1[i]+num2[i]
        print(sum)
        i+=1
add_number_list([50, 60, 10],[10, 20, 13])