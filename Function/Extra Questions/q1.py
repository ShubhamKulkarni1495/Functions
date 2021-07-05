#def update():
#    d4={}
#    d4.update(d1)
#    d4.update(d2)
#    d4.update(d3)
#    print(d4)

#d1={1:10, 2:20}
#d2={3:30, 2:40}
#d3={5:50,6:60}
#update()

#def sum():
#        d= {
#        'data1':100,
#        'data2': -54,
#        'data3': 247
#       } 
#        total=0
#        for i in d.values():
#            total+=i
#        return total
#print(sum())

#def combine():
#    list1=["one","two","three","four","five"]
#    list2=[1,2,3,4,5,]  
#    d={}
#    for i in list1:
#        for j in list2:
#            d[i]=j
#            list2.remove(j)
#            break
#    print(d)
#combine()

#def unique():
#     d=[
#     {"first":"1"}, 
#     {"second": "2"}, 
#     {"third": "1"}, 
#     {"four": "5"}, 
#     {"five":"5"}, 
#     {"six":"9"},
#     {"seven":"7"}
#        ]
#     a=[]
#     for i in d:
#         for j in i.values():
#             if j not in a:
#                 a.append(j) 
#     print(a)
#unique()   

#def student_marks(**x):
#    for i in range(num):
#        name=input("enter the name:") 
#        marks=int(input("enter the marks:"))
#        x[name]=marks
#    print(x) 
#num=int(input("how many inputs you want:"))  
#student_marks()

#def count(x):
#    length=0
#    for i in x:
#        length+=1
#    print(length)
#count([50, 40, 23, 70, 56, 12, 5, 10, 7])

#def count(x):
#   length=0
#   for i in x:
#       if i>=20 and i<=40:
#           length+=1
#   print(length)
#count([50, 40, 23, 70, 56, 12, 5, 10, 7])

#def count(x):
#    max=x[0]
#    for i in range(len(x)):
#        if max<x[i]:
#            max=x[i]
#            print(max)
#count([50, 40, 23, 70, 56, 12, 5, 20, 7])

   
#def count(x):
#    max1=x[0]
#    max2=x[0]
#    for i in range(len(x)):
#        if max1<x[i]:
#            max1=x[i]
#    for j in range(len(x)):
#        if max1>x[j] and max2<x[j]:
#            max2=x[j]
#    print(max2)
#count([50, 40, 23, 70, 56, 12, 5, 20, 67]) 

#def palindrome(x):
#    length=len(x)
#    reverse=""
#    while(length>0):
#        reverse+=x[length-1]
#        length-=1
#    if reverse == x:
#         print("it's a palindrome")
#    else:
#         print("not a palindrome")
#a=input("enter the input:")
#palindrome(a)

#def diff(x,y):
#    l1=[]
#    for i in x:
#        if i not in y:
#            l1.append(i)
#    print(l1)
#diff([1,2,3,4,5,6],[2,3,1,0,6,7])

#def add(x):
#    number=30
#    for i in range(len(x)-1):
#        for j in range(i+1,len(x)):
#            if x[i]+x[j] == number:
#                print("pair found",[x[i],x[j]])
#add([10, 11, 12, 13, 14, 17, 18, 19])

#def odd_even(x):
#    count=0
#    count1=0
#    for i in x:
#        if i%2==0:
#            count+=1
#        else:
#            count1+=1
#    print(count)
#    print(count1)
#odd_even([23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43])

#def sum(x):
#    sum1=0
#    sum2=0
#    for i in x:
#        if i%2 ==0:
#            sum1+=i
#        else:
#            sum2+=i
#    print(sum1)
#    print(sum2)
#sum([23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43])


#def sum_avg(x):
#    sum1=0
#    sum2=0
#    count1=0
#    count2=0
#    for i in x:
#        if i%2 ==0:
#            sum1+=i
#            count1+=1
#        else:
#            sum2+=i
#            count2+=1
#    avg1=sum1/count1
#    print(avg1)
#    avg2=sum2/count2
#    print(avg2)
#sum_avg([23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43])

#def kbc(q,o,s,l):
#    print("-----------WELCOME TO KBC-------------------")
#    i=0
#    count=0
#    sum=0
#    while(i<len(q)):
#        j=0
#        print("Your question is here---->")
#        print(q[i])
#        while(j<len(o[i])):
#            print(j+1,o[i][j])
#            j+=1
#        a=int(input("Enter your Answer Or Else You Can Use 5050--->"))
#        if(a == s[i]):
#            sum=sum+10000
#            print("Congratulations Your Answer Is Right And You Have Won--->",sum)
#        elif(a == 5050):
#            if(count==1):
#                print("Sorry You Have Already Used The 50/50 Lifeline")
#                a1=int(input("Enter Your Answer---->"))
#            if(count<1):
#                count+=1
#                print(l[i][0])
#                print(l[i][1])
#                a1=int(input("You Have Two Options Now Choose Corrcet Answer--->"))
#            if(a1 == s[i]):
#                sum=sum+10000
#                print("Congratulations Your Answer Is Right And You Have Won--->",sum)
#            else:
#                print("Your Answer Is Wrong You Lost-->",sum)
#                print("----Game Over-----")
#                break
#        else:
#            print("Your Answer Is Wrong You Lost---->",sum)
#            print("----Game Over-----")
#            break
#        i+=1
#kbc([
#    "1)How many continents are there?",        
#    "2)What is the capital of India?",          
#    "3)NG mei kaun se course padhaya jaata hai?" 
#],[
#    ["Four", "Nine", "Seven", "Eight"],
#    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
#    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
#],
#[3, 4, 1],
#[["1 eight\n","3 seven"],["2 Bhopal\n","4 Delhi"],["1 Software Engineering\n","3 Tourism"]])

#def magic(x):
#    row=0
#    col=0
#    d1=0
#    d2=0
#    i=0
#    while(i<len(x)):
#        j=0
#        while(j<len(x[i])):
#            row=row+x[i][j]
#            col=col+x[i][j]
#            d1=d1+x[j][j]
#            d2=d2+x[j][-j-1]
#            j+=1
#        i+=1
#    if(row==col==d1==d2):
#        print("it is a magic square")
#    else:
#        print("it is not a magic square")
#magic([
#    [8,3,4],
#    [1,5,9],
#    [6,7,2],
#])     