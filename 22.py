# Names scores
import time

start = time.time()
with open('names.txt') as f:
    names = sorted(f.read().replace('"', '').split(','))
    print(len(names))
    alphabet = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
        'N': 14,
        'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
    }
    # 867244018
    total = []
    for name in names:
        s = 0
        for letter in name:
            s += alphabet[letter]
        # print('sum of letters = ' + str(s))
        score = (names.index(name) + 1) * s
        total.append(score)
        # print(score)
    print(len(total))
    print(sum(total))
end = time.time()

print('Time of execution = ' + str(end - start))
