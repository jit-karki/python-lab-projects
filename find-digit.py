num = int(input("Enter a number: "))
n = abs(num) # handle negative numbers

# last digit
last_digit = n % 10

# first digit
first_digit = n
while first_digit >= 10:
    first_digit = first_digit // 10

print(f"Number: {num}")
print(f"First digit: {first_digit}")
print(f"Last digit: {last_digit}")