# loop prints 1..10
# 1. start? 
# 2. steps?
# 3. end?
print("BEFORE")
n = 1 #1. start

while n<=10: # 3. end
    print(n)
    n+= 1  # 2. steps

print("AFTER")

# H1: refactor the 10.9.9 ...10print("BEFORE")
n = 10 #1. start

while n >= 1: # 3. end
    print(n)
    n -= 1  # 2. steps

print("AFTER")



