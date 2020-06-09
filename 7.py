i = 3
shit_indicator = 0
simple_nums = [2]
while len(simple_nums) < 10001:
    for k in range(2, i):
        if i % k == 0:
            shit_indicator = 1
            break
    if shit_indicator == 1:
        pass
    else:
        simple_nums.append(i)
    i += 1
    shit_indicator = 0
print(simple_nums[-1])