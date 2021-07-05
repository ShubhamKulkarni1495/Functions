# ### example1:::
# def add_numbers_more(number_x, number_y):
#     number_sum = number_x + number_y
#     print ("Hello from NavGurukul ;)")
#     return number_sum
#     number_sum = number_x + number_x
#     print ("Kya main yahan tak pahunchunga?")
#     return number_sum
  
# sum1=add_numbers_more(100, 20)
# print(sum1)

### example 2:::
def menu(day):
    if day == "monday":
        return "Butter Chicken"
    elif day == "tuesday":
        return "Mutton Chaap"
    else:
        return "Chole Bhature"

    print ("Kya main print ho payungi? :-(")

mon_menu = menu("monday")
print (mon_menu)
tues_menu = menu("tuesday")
print (tues_menu)
fri_menu = menu("friday")
print (fri_menu)

### example 3:::

def menu(day):
    if day == "monday":
        food = "Butter Chicken"
    elif day == "tuesday":
        food = "Mutton Chaap"
    else:
        food = "Chole Bhature"
    print ("Kya main print ho payungi? :-(")
    print ("Lekin main toh pakka nahi print hounga :'(")
    return food
print(menu("monday"))

