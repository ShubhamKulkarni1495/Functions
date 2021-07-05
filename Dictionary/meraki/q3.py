my_dict={'data1':100,
        'data2': -54,
        'data3': 247
        }
print(my_dict) 
x=my_dict.values()
print(x)
y=sum(x)
print(y)

sum=0
for i in x:
    sum=sum+i
print(sum)
