from pymath.lib import is_prime, check_goldbach

while True:
    start_input = input("Enter the starting even number (or -1 to exit): ")
    if start_input == "-1":
        break

    try:
        start = int(start_input)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    end_input = input("Enter the ending even number: ")
    try:
        end = int(end_input)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if start == -1: # Should already be caught by the first check, but good for robustness
        break

    # Goldbach's conjecture applies to even integers > 2.
    # Adjust start if it's odd or too small.
    if start % 2 != 0:
        start += 1
    if start <= 2:
        start = 4 # Smallest even number > 2

    # Ensure end is not less than start
    if end < start:
        print(f"Ending number ({end}) cannot be less than starting number ({start}).")
        continue

    print(f"Checking Goldbach's conjecture for even numbers from {start} to {end}...")

    for n in range(start, end + 1, 2):
        if n <= 2: # Should be covered by start adjustment, but as a safeguard
            continue
        result = check_goldbach(n)
        if result:
            print(f"{n} = {result[0]} + {result[1]}")
            # print(f"{n} can be represented as the sum of two prime numbers") # This is redundant given the line above
        elif n > 2 and n % 2 == 0 : # Only print "cannot be represented" if it was a valid candidate
            print(f"{n} cannot be represented as the sum of two prime numbers by this check.")
        # If check_goldbach returned None because n was invalid (e.g. odd, <=2), we don't print a specific failure for Goldbach here,
        # as the loop structure and initial checks should handle it.
        # The current lib.check_goldbach returns None for invalid inputs as well.

    print("\nHeuristic Justification:")
    print("Goldbach's conjecture, which states that every even integer greater than 2 can be expressed as the sum of two prime numbers, has been numerically verified for all even numbers up to 4 × 10^18 (4 quintillion). However, it has not been formally proven for all even numbers.")
    print("The approach used in this code follows the general idea of checking if an even number can be represented as the sum of two prime numbers by iterating through all possible combinations. This method is effective for smaller ranges of even numbers, but it becomes computationally expensive for larger ranges due to the need to check each even number individually.")
    print("While this method does not provide a definitive proof of Goldbach's conjecture, it can be used to gain insights into the behavior of even numbers and their representation as the sum of two prime numbers. The heuristic justification suggests that the conjecture is highly likely to be true, even though a formal mathematical proof remains elusive.")
