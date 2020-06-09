n = 100
mult = 1
while n > 1:
    mult *= n
    n -= 1
s = 0  # sum
while mult > 0:
    digit = mult % 10
    s += digit
    mult = mult // 10
print(s)
