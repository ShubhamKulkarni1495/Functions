x={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
sort=sorted(x.values())
dic={}
for i in sort:
    for j in x.keys():
        if x[j]==i:
            dic[j]=x[j]
            break
print(dic)


x={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
sort=sorted(x.values(),reverse=True)
dic={}
for i in sort:
    for j in x.keys():
        if x[j]==i:
            dic[j]=x[j]
            break
print(dic)