fibo = [1, 2]
fibo_2 = []

i = 0

while True:
    a = fibo[-2] + fibo[-1]
    fibo.append(a)
    i += 1
    if a > 4000000:
        del fibo[-1]
        break

print(fibo)

for c in fibo:
    print(c)
    if c % 2 == 0:
        fibo_2.append(c)

print(sum(fibo_2))