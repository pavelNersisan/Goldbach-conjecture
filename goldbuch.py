def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_goldbach(n):
    for i in range(2, int(n/2)+1):
        if is_prime(i) and is_prime(n-i):
            print(f"{n} = {i} + {n-i}")
            return True
    return False

while True:
    start = int(input("Enter the starting even number (or -1 to exit): "))
    if start == -1:
        break

    end = int(input("Enter the ending even number: "))

    # If the starting number is odd, add 1 to make it even
    if start % 2 != 0:
        start += 1

    # Check each even number within the range
    for n in range(start, end+1, 2):
        if check_goldbach(n):
            print(f"{n} can be represented as the sum of two prime numbers")
        else:
            print(f"{n} cannot be represented as the sum of two prime numbers")

    # Heuristic justification
    print("\nHeuristic Justification:")
    print("Goldbach's conjecture, which states that every even integer greater than 2 can be expressed as the sum of two prime numbers, has been numerically verified for all even numbers up to 4 × 10^18 (4 quintillion). However, it has not been formally proven for all even numbers.")
    print("The approach used in this code follows the general idea of checking if an even number can be represented as the sum of two prime numbers by iterating through all possible combinations. This method is effective for smaller ranges of even numbers, but it becomes computationally expensive for larger ranges due to the need to check each even number individually.")
    print("While this method does not provide a definitive proof of Goldbach's conjecture, it can be used to gain insights into the behavior of even numbers and their representation as the sum of two prime numbers. The heuristic justification suggests that the conjecture is highly likely to be true, even though a formal mathematical proof remains elusive.")
