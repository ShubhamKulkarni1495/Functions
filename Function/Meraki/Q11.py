def check_speed(limit):
    if limit<70:
        print("Speed limit is OK")
    elif limit>=70:
        count=0
        for i in range(70,limit):
            if i%5==0:
                count+=1
        if count>12:
            print("Your Licensce Is Suspended")
        else:
            print(count)
limit=int(input("Enter the speed:"))
check_speed(limit)