num = int(input("Enter a number: "))
n = abs(num)  # to handle negative numbers

if n == 0:
    product = 0
else:
    product = 1
    while n > 0:
        digit = n % 10
        product *= digit
        n = n // 10

print(f"Product of digits of {num} is {product}")