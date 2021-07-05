def reverse():
    str1="1234abcd"
    str2=""
    length=len(str1)
    while length>0:
        str2+=str1[length-1]
        length-=1
    print(str2)
reverse()


def string_reverse(str1):

    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
print(string_reverse('1234abcd'))

