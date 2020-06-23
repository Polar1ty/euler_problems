# Highly divisible triangular number
import time
from math import sqrt

start = time.time()

triangular_nums = []

# Triangular number generator
for n in range(100000):
    triangular_nums.append(int((n * (n + 1)) / 2))

dividers = 2

for num in triangular_nums:
    if dividers > 500:
        break
    else:
        print(num)
        dividers = 2
        for i in range(2, int(sqrt(num)) + 1):  # count quantity of dividers
            if dividers > 500:
                print('Result -->', num)
                break
            if num % i == 0:
                dividers += 2

end = time.time()
print('Time of execution = ' + str(end - start))

