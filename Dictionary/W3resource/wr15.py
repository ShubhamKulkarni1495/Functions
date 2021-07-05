my_dict = {'x':500, 'y':5874, 'z': 560}
list1=[]
for i in my_dict.values():
    list1.append(i)
print(list1)
max=list1[0]
min=list1[0]
for i in range(len(list1)):
    for j in range (len(list1)):
        if list1[j]>max:
            max=list1[j]
        if list1[j]<min:
            min=list1[j]
print(max)
print(min)