sum_sqr = 0
sqr_sum = 0
for i in range(1, 101):
    sum_sqr += (i * i)
    sqr_sum += i
print(sqr_sum * sqr_sum - sum_sqr)