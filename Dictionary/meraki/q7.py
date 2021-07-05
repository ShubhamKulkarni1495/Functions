x= [
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
]
y={}
z=[]
for i in x:
    y.update(i)
for i in y.values():
    if i not in z:
        z.append(i)
print(z)