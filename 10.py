# Summation of primes
import time
from math import sqrt

start = time.time()

n = 2000000
lst = []
for i in range(2, n+1):
    print(i)
    for j in lst:
        if i % j == 0:
            break
    else:
        lst.append(i)
print(sum(lst))

end = time.time()
print('Time of execution = ' + str(end - start))
