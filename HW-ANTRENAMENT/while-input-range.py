start = int(input("Enter the start number: "))
end = int(input("Enter the end of number: "))
while True:
    if start <= end:
        for num in range(start, end + 1):
            print(num, end = " ")
    elif start >= end:
        for num in range(start, end - 1,-1):
            print(num, end = " ")
    break        