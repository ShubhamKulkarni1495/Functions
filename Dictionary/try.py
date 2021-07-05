n=int(input("enter the range:"))
i=1
while i<=n*2:
    if i%2==0:
        print(i)
    i+=1
    

# a="hello"
# c=0
# for i in a:
#     f=0
#     if "a"==i or "e"==i or "i"==i or "o"==i or "u"==i:
#         g=0
#         for k in range(1,c*100):
#             r=0
#             for j in range(2,k):
#                 if k%j==0:
#                     e=i
#                     r+=1
#             if r==0:
#                 g+=k
#         yy=0
#         for l in str(g-1):
#             yy+=int(l)
#         a=a.replace(i,str(yy))
#     c+=1
# print(a)