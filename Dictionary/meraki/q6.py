dic={
    "ball":"red",
    "bat":4,
    "wickets":8,
    "ball":"green",
    "bat":3
    }
print(dic)

y={}
for key,val in dic.items():
    if val not in y.values():
        y[key]=val
print(y)