def check_goldbach(n):
    # Check if n is even
    if n % 2 != 0:
        return False

    # Check if n can be represented as the sum of two primes
    for i in range(2, n):
        if is_prime(i) and is_prime(n - i):
            return True

    return False

def is_prime(n):
    # Check if n is a prime number
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

# Get the range of even numbers from the user
start = int(input("Enter the starting even number: "))
end = int(input("Enter the ending even number: "))

# If the starting number is odd, add 1to make it even
if start % 2 != 0:
    start += 1

# Check each even number within the range
for n in range(start, end+1, 2):
    if check_goldbach(n):
        print(f"{n} can be represented as the sum of two prime numbers")
