# 1000-digit Fibonacci number

fibo = [0, 1, 1]  # Zero added to see real index of 1000-digit number according to task

while 1:
    new_f = fibo[-2] + fibo[-1]
    fibo.append(new_f)
    if len(str(new_f)) == 1000:
        print('Result =', fibo.index(new_f))
        break
