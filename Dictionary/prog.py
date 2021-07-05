# a=["h","e","l","l","o"]
# b='aeiou'
# for i in a:
#     if i in b:
#         c=a.index(i)
#         d=0
#         for i in range(1,c*100,1):
#             e=0
#             for j in range(2,i):
#                 if i%j==0 and j!=1:4
#                     e=1
#             if e==0:
#                 d+=i
#         d=str(d-1)
#         f=sum(int(e) for e in d)
#         f=str(f)
#         a.remove(a[c])
#         a.insert(c,f)
# print(a)



a="siddik"
b="aeiou"
c=0
for i in a:
    if i in b:
        sum=0
        for k in range(1,c*100):
            r=0
            for j in range(2,k):
                if k%j==0:
                    r+=1
            if r==0:
                sum+=k
        yy=0
        for l in str(sum-1):
            yy+=int(l) 
        a=a.replace(i,str(yy))
    c+=1
print(a)

