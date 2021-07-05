n=[1,2,3,[4],[5,6,"a"],7,["d"],"g",5,333,[33,55,"n"]]
for i in range(len(n)):
    for i in n:
        if type(i)==list:
            n.remove(i)
            for j in i:
                n.append(j)
print(n)
print()