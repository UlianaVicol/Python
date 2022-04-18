
rows = 5
i    = 1
while i <= rows:
    j = i
    while j < rows:
        print(" ", end=" ")
        j += 1
    k = 1
    while k <= i:
        print("*", end=" ")
        k += 1
    print()
    i += 1
i = rows
while i >= 1:
    j = i
    while j <= rows:
        print(" ", end=" ")
        j += 1
    k = 1
    while k < i:
        print("*", end=" ")
        k += 1
    print('')
    i -= 1

n = 5
i = n
while i>1:
    print(" "*(n-i) + "* " * i)
    i-=1
i = 1
while i<=n:
    print(" "*(n-i) + "* " * i)
    i+=1