# swap 2 indexes in a List 

values = [10,20,30,40,50,60,70]
#             ^        ^
# index       1        4
#            ia        ib

ia = int(input("first: "))
ib = int(input("second: "))

print("Before:" , values)
values[ib],values[ia] = values[ia],values[ib]
print("After:" , values)