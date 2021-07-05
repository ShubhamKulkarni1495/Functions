d=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
dic={}
for i in d:
    for j,k in i.items():
        if j in i:
            dic[j]=k
print(dic)
