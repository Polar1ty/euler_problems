# Coin sums

combs = 0

for i in range(201):
    for j in range(101):
        for k in range(81):
            for a in range(21):
                for b in range(11):
                    for c in range(5):
                        for d in range(3):
                            for e in range(2):
                                if i * 1 + j * 2 + k * 5 + a * 10 + b * 20 + c * 50 + d * 100 + e * 200 == 200:
                                    print(combs)
                                    combs += 1
print('Result =', combs)

