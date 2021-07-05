def counters(a):
    x={"count":0,"count1":0}
    for i in a:
        if i.isupper():
            x["count"]+=1
        elif i.islower():
            x["count1"]+=1
        else:
            pass
    print("Number of Upper case letters:",x["count"])
    print("Number of Lower case letters:",x["count1"])
counters('The quick Brown Fox')
