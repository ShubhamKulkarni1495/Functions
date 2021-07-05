def eligible_for_vote(age):
    if age>=18:
        print("Eligible For Vote")
    else:
        print("Not Eligible For Vote")
age=int(input("Enter your age:"))
eligible_for_vote(age)