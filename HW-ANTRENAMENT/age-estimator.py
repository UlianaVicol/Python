currentYear   = 2022
yearBirth     = int(input("Year of birth: "))


age           = currentYear - yearBirth
if yearBirth < 1900:
    print("Old ))")
elif yearBirth > currentYear: 
    print("Young :) yeeee")

if age < 4:
    print("baby and you have:", age)
elif age < 10:
    print("kid, you have:", age)
elif age < 16:
    print("teen, you have:", age, "I miss those times...")
elif age < 19:
    print("young, you have:", age, "don't be lazy )")
elif age < 51:
    print("adult, you have:", age, " still young ;)")
else:
    print("old, you have:", age, "HMMMMMMMMMM, that's life... ;)")
