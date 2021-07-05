### part1:::
def student(*name):
    i=0
    while i<len(name):
        print(i+1,"student name is",name[i])
        i+=1
student("Vikas","Rajesh","Sai Kiran","Shubham")

### part2:::
def isGreaterThan20(a=0,b=0):
    print(a,"and",b)
isGreaterThan20(20)