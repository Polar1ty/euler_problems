# Lexicographic permutations
import time
start = time.time()

nums1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def permutations(arr):
    combs = []
    for a in arr:
        if len(combs) > 1000002:
            print('Result =', combs[999999])
            break
        for b in arr:
            for c in arr:
                for d in arr:
                    for e in arr:
                        for f in arr:
                            for g in arr:
                                for h in arr:
                                    for i in arr:
                                        for j in arr:
                                            if a != b and a != c and a != d and a != e and a != f and a != g and a != h and a != i and a != j and b != c and b != d and b!=e and b!=f and b!=g and b!=h and b!=i and b!=j and c!=d and c!=e and c!=f and c!=g and c!=h and c!=i and c!=j and d!=e and d!=f and d!=g and d!=h and d!=i and d!=j and e!=f and e!=g and e!=h and e!=i and e!=j and f!=g and f!=h and f!=i and f!=j and g!=h and g!=i and g!=j and h!=i and h!=j and i!=j:
                                                combs.append(a+b+c+d+e+f+g+h+i+j)
                                                print(len(combs))




permutations(nums1)
end = time.time()
print('Time of execution = ' + str(end - start))  # Takes around 10 minutes..
