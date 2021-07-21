# def fun1():
#     s="Nav"
#     def fun2():
#         print(s+"Gurukul")
#     fun2()
# fun1()

def fun1():
    s=first
    def fun2():
        print(s+second)
    second=input("Enter a String:")
    fun2()
first=input("Enter a First String:")
fun1()