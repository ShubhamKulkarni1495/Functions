# number =int(input("Enter integer: "))
# thousand= [ "", "M", "MM", "MMM" ]
# hundred= [ "", "C", "CC", "CCC", "CD", "D","DC", "DCC", "DCCC", "CM "]
# tenth= [ "", "X", "XX", "XXX", "XL", "L","LX", "LXX", "LXXX", "XC" ]
# ones= [ "", "I", "II", "III", "IV", "V","VI", "VII", "VIII", "IX"]
# TD = thousand[number// 1000]
# HD= hundred[(number % 1000) // 100]
# TN=  tenth[(number % 100) // 10]
# OS= ones[number % 10]     
# ROMAN= (TD+HD+TN+OS)   
# print(ROMAN, "is the roman value of", number)


number=int(input("Enter the number to Convert:"))
dic={1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"XD",500:"D",900:"CM",1000:"M"}

order=[1000,900,500,400,100,90,50,40,10,9,5,4,1]

for i in order:
    if number!=0:
        a=number//i
        
        if a!=0:
            for j in range(a):
                print(dic[i],end="")
    number=number%i
print()
