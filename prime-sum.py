n = int(input("enter the nth term: "))

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

total = 0
for num in range(2, n + 1):
    if is_prime(num):
        total += num

print(f"Sum of prime numbers from 1 to {n} is: {total}")