n = 600851475143
prime_factor = 1
i = 2

while i <= n / i:
    if n % i == 0:
        prime_factor = i
        n /= i
    else:
        i += 1
if prime_factor < n:
    prime_factor = n

print(prime_factor)