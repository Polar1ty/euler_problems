# Digit factorials

import time

start = time.time()

curious_nums = []

for i in range(3, 100000):
    f_sum = 0
    ic = i
    while i > 0:
        digit = i % 10
        factorial = 1
        while digit > 1:
            factorial *= digit
            digit -= 1
        f_sum += factorial
        i = i // 10
    if f_sum == ic:
        curious_nums.append(ic)
print(sum(curious_nums))

end = time.time()
print('Time of execution = ' + str(end - start))