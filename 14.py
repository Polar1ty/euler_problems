def collatz(n):
    seq = [n]
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            seq.append(int(n))
        else:
            n = 3 * n + 1
            seq.append(int(n))
    return len(seq)


i = 1
seqs = []
dictich = {}
while i < 1000000:
    length = collatz(i)
    dictich[length] = i
    seqs.append(length)
    i += 1
max_len = max(seqs)
print(dictich[max_len])


