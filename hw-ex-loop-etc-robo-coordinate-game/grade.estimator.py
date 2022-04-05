# IN: student's grade 1..10
# out: good, ok, bad grade

# x ---> x ---> x ---> x
# 1      5      7      10
grade = int(input("Your grade:"))

if grade >7 and grade <=10:
    print("GOOD!")
elif grade > 4 and grade <=7:
    print("ok!")
elif grade >= 1 and grade <=4:
    print("bad!")
else:
    print("wrong value! :(")

#HW1: continuu with  - WRONG VALUE 