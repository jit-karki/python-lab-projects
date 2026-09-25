num = int(input("Enter a number: "))

# work with absolute value to handle negative numbers
n = abs(num)

if n == 0:
    count = 1
else:
    count = 0
    while n > 0:
        n = n // 10
        count += 1

print(f"Number of digits in {num} is {count}")