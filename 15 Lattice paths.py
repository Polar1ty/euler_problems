# Lattice paths

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


n = 20

print(int(factorial(2 * n) / (factorial(n) * factorial(n))))
