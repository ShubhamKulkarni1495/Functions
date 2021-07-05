word='w3resource'
x={}
for i in word:
    c=word.count(i)
    x[i]=c   
print(x)

word="w3resource"
x={}
list1=list(word)
list2=[]
for i in range(len(list1)):
    if list1[i] not in list2:
        list2.append(list1[i])
for i in range(len(list2)):
    count=0
    for j in range(len(list1)):
        if list2[i]==list1[j]:
            count+=1
    x[list2[i]]=count
print(x)
