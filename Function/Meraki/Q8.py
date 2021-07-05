def sum_avg(x,y,z):
    sum=x+y+z
    print(sum)
    avg=sum/3
    print(avg)
sum_avg(10,20,30)

def sum_avg():
    sum=0
    for i in range(3):
        num=int(input("Enter the numbers:"))
        sum+=num
    print(sum)
    avg=sum/3
    print(avg)
sum_avg()