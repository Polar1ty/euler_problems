i = 2 ** 1000
s = 0
while i > 0:
    digit = i % 10
    s += digit
    i = i // 10
print(s)