def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_goldbach(n):
    # Ensure n is an even number greater than 2 for Goldbach's conjecture
    if n <= 2 or n % 2 != 0:
        # In a library, it's better to return a clear indicator of invalid input or raise an exception.
        # For now, let's return None, and the caller can decide how to message it.
        return None
    for i in range(2, int(n/2)+1):
        if is_prime(i) and is_prime(n-i):
            return (i, n-i) # Return the pair
    return None # Return None if no such pair is found

def gcd(a, b):
    """Calculates the Greatest Common Divisor (GCD) of two integers."""
    a = abs(a)
    b = abs(b)
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Calculates the Least Common Multiple (LCM) of two integers."""
    if a == 0 or b == 0:
        return 0
    val_gcd = gcd(a, b)
    # This check for val_gcd == 0 is redundant if gcd always returns non-negative,
    # and gcd of (0,0) is 0. If a or b is 0, then gcd(a,b) could be non-zero
    # (e.g. gcd(0,5)=5). The original code handles a=0 or b=0 by returning 0 for lcm.
    # If gcd is 0 (only if a and b are 0), then a*b is also 0.
    # To avoid ZeroDivisionError if gcd could be 0 when a*b is not, this check is fine.
    # However, standard gcd(0,0) is often defined as 0.
    # If gcd guarantees non-zero for non-zero a,b, then this check isn't strictly needed.
    # For safety, keeping a check or ensuring gcd handles (0,0) appropriately.
    # Given the current gcd, if a=0 and b=0, gcd(0,0) = 0. Then (0*0)//0 causes ZeroDivisionError.
    # The initial check `if a == 0 or b == 0: return 0` correctly handles this.
    # So, val_gcd will not be 0 if a or b was non-zero.
    # If both a and b are zero, it returns 0 before this point.
    # Thus, val_gcd here will be non-zero if we reach here.
    return abs(a * b) // val_gcd

def factorial(n):
    """Calculates the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0:
        return 1
    else:
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res
