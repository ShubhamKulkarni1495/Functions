list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]
x={}
for keys in list1:
    for values in list2:
        x[keys]=values
        list2.remove(values)
        break
print(x)

