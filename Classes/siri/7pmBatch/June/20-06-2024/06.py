# Generate a list of prime numbers up to a given number n.

n = 50
primes = [num for num in range(2, n + 1) if all(num % div != 0 for div in range(2, int(num**0.5) + 1))]
print(primes)

