a = range(1, 1000)
b = range(1, 1000)

mlt = []
palyndroms = []

for i in a:
    for x in b:
        mlt.append(i * x)

for num in mlt:
    if str(num) == str(num)[::-1]:
        palyndroms.append(num)

print(max(palyndroms))