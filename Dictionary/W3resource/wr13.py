keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
dic={}
for i in keys:
    for j in values:
        dic[i]=j
print(dic)

keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
dic=dict(zip(keys,values))
print(dic)