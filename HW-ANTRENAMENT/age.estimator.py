currentYear   = 2022
yearBirth     = int(input("Insert your year of birth: "))


age           = currentYear - yearBirth
if yearBirth < 1900:
    print("too old")
elif yearBirth > currentYear: 
    print("too young :) yeeee")

if age < 4:
    print("baby and you have:", age, ":) ")
elif age < 10:
    print("kid, you have:", age, "go outside! Now!!!")
elif age < 16:
    print("teen, you have:", age, "I miss those times...")
elif age < 19:
    print("young, you have:", age, "don't be lazy )")
elif age < 51:
    print("adult, you have:", age, " you're still young, bro")
else:
    print("old, you have:", age, "HMMMMMMMMMM bro, that's life... :(  ;)")