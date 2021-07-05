word="MISSISSIPPI"
x={}
count=0
for i in word:
    if i not in x:
        count=count+1
        x[i]=count   
print(x)