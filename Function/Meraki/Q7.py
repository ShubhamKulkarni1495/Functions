### for loop:::
def perfect():
    for i in range(1,1000):
        sum=0
        for j in range(1,i):
            if i%j==0:
                sum+=j
        if sum == i:
            print(i,"Its a Perfect Number")
perfect()

### While loop:::
def perfect():
    i=1
    while i<=1000:
        sum=0
        j=1
        while j<i:
            if i%j==0:
                sum+=j
            j+=1
        if sum == i:
            print(i,"Its a Perfect Number")
        i+=1
perfect()