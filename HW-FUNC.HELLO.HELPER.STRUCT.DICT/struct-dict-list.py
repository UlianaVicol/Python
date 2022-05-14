# Input (kb) >> struct >> Output (console)
# template dictionary

person = {
    "full name": "Enter your full name",
    "city": "Your city?",
    "street": "Your street?",
}

# INPUT data
for key in person:
    person[key] = input( person[key] + ": ")

# OUTPUT data
for key in person:
    print(f"{key:>15}: {person[key]:20}")