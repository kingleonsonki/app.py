def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_primes(start, end):
    """Return a list of prime numbers in the given range [start, end]."""
    return [x for x in range(start, end + 1) if is_prime(x)]


if __name__ == "__main__":
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))
    primes = find_primes(start, end)
    print(f"Prime numbers between {start} and {end}: {primes}")
