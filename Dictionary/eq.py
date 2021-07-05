# d={'a':1,'b':1,'c':2,'d':3,'e':3, 'l':1, 'g':6}
# x={}
# for i,j in d.items():
#     if j not in x:
#         x[j]=[i]
#     else:
#         x[j].append(i)
# print(x)

f=0
for k in range(1,10):
    e=0
    for j in range(2,k):
        if k%j==0:
            break
        else:
            e=k
    print(e)
    f+=e
print(f)
