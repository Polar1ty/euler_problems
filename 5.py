# Smallest multiple
import time

start = time.time()
for i in range(1, 1000000000):
    if i % 11 == 0 and i % 12 == 0 and i % 13 == 0 and i % 14 == 0 and i % 15 == 0 and i % 16 == 0 and i % 17 == 0 and i % 18 == 0 and i % 19 == 0 and i % 20 == 0:
        print(i)

end = time.time()
print('Time of execution = ' + str(end - start))
