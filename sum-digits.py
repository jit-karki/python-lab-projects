num = int(input("Enter a number: "))
n = abs(num)  # handle negative numbers

total = 0
if n == 0:
    total = 0
else:
    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10

print(f"Sum of digits of {num} is {total}")