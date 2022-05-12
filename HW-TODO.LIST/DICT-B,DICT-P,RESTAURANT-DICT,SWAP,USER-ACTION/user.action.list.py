# using the list as Stack

# app -> remembers User Action History

# Lifo

ua = []

while True:
    action = input("Enter an action name: ")
    if action == "":
        break
    ua.append(action)

steps = len(ua)
print("You've Made: ", steps, " steps")
retrace_steps = int(input("How many to go back?"))

# not longuer than total number of steps
while len(ua) > 0 or retrace_steps != 0:
    action = ua.pop( len(ua)-1)  # cut the element
    print("delete step >>" , action)
    retrace_steps -= 1

print(ua)