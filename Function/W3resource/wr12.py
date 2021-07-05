def palindrome(x):
    length=len(x)
    new=""
    while length>0:
      new+=x[length-1]
      length-=1
    if x==new:
        print("it is palindrome")
    else:
        print("it is not a palindrome")
palindrome("nitin")

def palindrome():
    length=len(x)
    new=""
    while length>0:
      new+=x[length-1]
      length-=1
    if x==new:
        print("it is palindrome")
    else:
        print("it is not a palindrome")
x=input("Enter the input:")
palindrome()