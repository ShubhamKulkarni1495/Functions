def mul():
    x=[8, 2, 3, -1, 7]
    mult=1
    for i in x:
        mult=mult*i
    print(mult)
mul()

def mul(x):
    mult=1
    for i in x:
        mult=mult*i
    return mult
print(mul((8, 2, 3, -1, 7)))    
