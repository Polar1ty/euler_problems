# 1000-digit Fibonacci number
import time

start = time.time()
fibo = [1, 1]

while 1:
    new_f = fibo[-2] + fibo[-1]
    fibo.append(new_f)
    if len(str(new_f)) == 10000:
        print('Result =', fibo.index(new_f) + 1)
        break

end = time.time()
print('Time of execution = ' + str(end - start))
