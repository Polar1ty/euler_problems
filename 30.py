all_nums = []
for i in range(10, 1000000):
    total = 0
    for l in str(i):
        total += int(l) ** 5
    if int(total) == int(i):
        all_nums.append(int(total))
print(sum(all_nums))