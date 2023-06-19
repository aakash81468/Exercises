def sum_of_prime_numbers(limit):
    # Create a boolean array to mark numbers as prime or not
    is_prime = [True] * limit

    # Mark 0 and 1 as non-prime
    is_prime[0] = is_prime[1] = False

    #Sieve of Eratosthenes algorithm
    p = 2
    while p * p < limit:
        if is_prime[p]:
            for i in range(p * p, limit, p):
                is_prime[i] = False
        p += 1

    # Calculating sum of prime numbers
    prime_sum = sum(num for num in range(limit) if is_prime[num])

    return prime_sum

# Calculating sum of primes below 200,000
limit = 200000
prime_sum = sum_of_prime_numbers(limit)

print("Sum of primes below", limit, ":", prime_sum)
